import json
import discord
import requests
from tokens import STEAM_API_KEY
import random
import string
import pandas as pd
from Administrative.channel_data import MEMBER_ROLE


# This whole process will ask users to enter a command for their steam profiles, upon successful request, the user
# is stored into a .csv with a token which the bot will check if the user entered their token on their steam accounts
# TODO: maybe look into implementing an actual database, but idc.
async def verify_user(steam_id64, message, client):
    shortlist = pd.read_csv('Administrative/unverifiedusers.csv')
    user = str(message.author)

    if user in shortlist.loc[:, 'userName'].tolist():
        if await check_credentials(user, shortlist):
            await assign_role(message, client)
            shortlist = shortlist[shortlist.userName == user]
            shortlist.to_csv('Administrative/unverifiedusers.csv', mode='w', header=False, index=False)
        return 0

    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + STEAM_API_KEY + '&steamids=' + steam_id64
    res = requests.get(url)

    if res.status_code == 200:
        user_token = "".join(random.sample(string.ascii_letters, 10))
        good_response = "Link checks out, I'll DM what you need to do from here."
        instructions = "Put this token into the 'real name' section of your steam profile, I'll either get back " \
                       "to you or you can call me again with .$ verify to confirm that it's really you on steam. \n" \
                       "```" + \
                       user_token + \
                       "```"
        await enter_user(user, user_token, url)

        await client.send_message(message.channel, good_response)
        try:
            await client.send_message(message.author, instructions)
        except message.HTTPException:
            error_instructions = "Sorry @" + user + " , I couldn't DM you so here are your instructions here instead."
            await client.send_message(message.channel, error_instructions)
    else:
        error_message = "Sorry " + user + ", that wasn't a valid steam profile provided, please provide a link" \
                                                 "similar to this: http://steamcommunity.com/profiles/76561197960287930"
        await client.send_message(message.channel, error_message)


async def check_credentials(user, shortlist):
    url = shortlist.loc[shortlist['userName'] == user, 'steamProfile'].tolist()[0]
    token = shortlist.loc[shortlist['userName'] == user, 'token'].tolist()[0]
    print(user, url, token)
    res = requests.get(url)
    user_data = res.json()
    realname = user_data['response']['players'][0]['realname']
    if token in realname:
        return True
    else:
        return False


async def enter_user(user, token, url):
    entry = pd.DataFrame([[user, url, token]], columns=['userName', 'steamProfile', 'token'])
    entry.to_csv('Administrative/unverifiedusers.csv', mode='a', header=False, index=False)


async def assign_role(message, client):
    role = discord.utils.get(message.server.roles, id=MEMBER_ROLE)
    print(role)
    try:
        if role in message.author.roles:
            await client.send_message(message.channel,
                                      "You already have the Member role! >:(")
            return 0
        await client.add_roles(message.author, role)
        await client.send_message(message.channel, "Welcome " + str(message.author) + ", your role has been assigned.")
    except discord.Forbidden:
        await client.send_message(message.channel, "I lack permissions to assign that role, go bother an admin please")

    return 0
