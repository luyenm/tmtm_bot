import pandas as pd
import discord
import asyncio
from Administration.channel_data import DEAD_ROLE, MOD_CHANNEL, MEMBER_ROLE
import random


async def infodump(message, client):

    await client.send_message(message.author, "Hi there! I'm TMTM's discord bot, developed by Arlios, while I'm still a"
                                              "a work in progress, I do have some commands available for you"
                                              "\n\n use \".?\" to get my attention, followed by the following commands."
                                              "\n 1) \"verify\" is used for new discord members to assign the member role."
                                              "\n 2) \"register mission\" is used by map makers, futher implementation is"
                                              "planned.")


# Clears the list of unverified users, re-prompts all users in the list to verify their identities.
async def clear_verifications(message, client):
    return


# Deletes a specified number of messages
async def delete_messages(number, message, client):
    messages = []
    number_of_messages = int(number)
    async for i in client.logs_from(message.channel, limit=number_of_messages):
        messages.append(i)
    await client.delete_messages(messages)
    await client.send_message(client.get_channel(MOD_CHANNEL), message.author.mention + " requested " + number + " deleted messages")
    return


# Kills half the server
# Picks a random half of the server to kill off
async def genocide(server_members, client, message):
    print(server_members)
    print("Number of members in server:", len(server_members))
    victims = int(len(server_members) / 2)
    dead_role = discord.utils.get(message.server.roles, id=DEAD_ROLE)
    member_role = discord.utils.get(message.server.roles, id=MEMBER_ROLE)
    for i in range(victims):
        victim = random.randint(1, int(len(server_members)))
        dead_boi = await client.get_user_info(server_members[victim].id)
        print(dead_boi.name, "died")
        await client.add_roles(server_members[victim], dead_role)
        await client.remove_role(server_members[victim], member_role)
        await asyncio.sleep(2)
    return


# Revives half the server
# Loops through all members
async def revive(server_members, client, message):
    dead_role = discord.utils.get(message.server.roles, id=DEAD_ROLE)
    member_role = discord.utils.get(message.server.roles, id=MEMBER_ROLE)
    for i in server_members:
        if any(roles.id in DEAD_ROLE for roles in server_members[i].roles):
            await client.add_roles(server_members[i], member_role)
            await client.remove_roles(server_members[i], dead_role)
    return
