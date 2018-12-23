import discord as ds
import os
from tokens import KEY, TOKEN, CLIENT
import Administration.channel_filter as cf
import Administration.user_verification as uv
import Administration.administrative_functions as af
import Features.secret_santa as ss
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

        if message.content[:2] == '.?' and str(message.author) in list(map(str, server.members)):
            request = message.content[2:]
            if 'verify' in request:
                await uv.verify_user(request.rsplit('profiles/', 1)[-1], message, client)
                return
            if 'register mission' in request.lower():
                if MISSION_MAKER in message.author.roles:
                    await client.send_message(message.channel, 'Yes queen')
                else:
                    await client.send_message(message.channel, 'Sorry, you\'re not special enough '
                                              + SMUG[random.randint(0, len(SMUG) - 1)])
                return
            if 'help' in request.lower():
                await af.infodump(message, client)
                return

            if ADMINISTRATIVE_ROLES in message.author.roles:
                if 'register secret santa' in request.lower():
                    await client.send_message(message.channel, 'WIP')
                if 'ping op':
                    await client.send_message(client.get_channel('362288299978784768'), client.get_user_info('134830326789832704').mention + 'come for the op')
        await sp.get_text(message, client)


@client.event
async def on_member_join(member):
    if member.server.id == AUTHORIZED_SERVER:
        await client.send_message(client.get_channel(CHECK_IN_CHANNEL),
                                  "Welcome to The Meme Team Marines " + member.mention + ", To gain access "
                                  "to the server, please type .$verify <link-to-your-steam-profile>. "
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
