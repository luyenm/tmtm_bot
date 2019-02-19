import discord as ds
import os
from tokens import KEY, TOKEN, CLIENT
import Administration.channel_filter as cf
import Administration.user_verification as uv
import Administration.administrative_functions as af
import Meme.shitpost as sp
from Administration.channel_data import MOD_CHANNEL, AUTHORIZED_SERVER, CHECK_IN_CHANNEL, ADMINISTRATIVE_ROLES,\
    MISSION_MAKER
from Meme.imgurlinks import SMUG
client = ds.Client()
import random


@client.event
async def on_read():
    print("Started")


@client.event
async def on_message(message):
    server = client.get_server(AUTHORIZED_SERVER)
    if message.author != client.user:
        if cf.checkphrase(message):
            await profanity_check(message)
            await client.delete_message(message.id)

        if message.content[:2] == '.?' and str(message.author) in list(map(str, server.members)):

            request = message.content.replace('.?', '').split()
            request.append(None)
            print(request)
            if 'verify' in request:
                print(message.author, 'request')
                url = ''
                if request[1] is not None:
                    url = request[1]
                await uv.verify_user(url, message, client)
                return
            if 'register mission' in request:
                if MISSION_MAKER in message.author.roles:
                    await client.send_message(message.channel, 'Yes queen')
                else:
                    await client.send_message(message.channel, 'Sorry, you\'re not special enough '
                                              + SMUG[random.randint(0, len(SMUG) - 1)])


                return

            if 'help' in request:
                await af.infodump(message, client)
                return

            if any(roles.id in ADMINISTRATIVE_ROLES for roles in message.author.roles):
                print("Admin request")
                if 'delete' in request:
                    if request[1] is not None:
                        await af.delete_messages(request[1], message, client)

                if 'test' in request:
                    await af.genocide(list(server.members), client, message)
            return
        await sp.get_text(message, client)


@client.event
async def on_member_join(member):
    if member.server.id == AUTHORIZED_SERVER:
        await client.send_message(client.get_channel(CHECK_IN_CHANNEL),
                                  "Welcome to The Meme Team Marines " + member.mention + ", To gain access "
                                  "to the server, please type .?verify <link-to-your-steam-profile>. "
                                  "If you are not in TMTM at the moment, "
                                  "please go through the regular application process to join.")


async def profanity_check(message):
    bad_user = str(message.author)
    caught_phrase = str(message.content)
    channel = str(message.channel)
    timestamp = str(message.timestamp)
    bad_message = bad_user, channel, caught_phrase, timestamp
    await client.delete_message(message)
    await client.send_message(client.get_channel(MOD_CHANNEL), bad_message)

client.run(TOKEN)

