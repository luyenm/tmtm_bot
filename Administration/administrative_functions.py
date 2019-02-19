import pandas as pd
from Administration.channel_data import DEAD_ROLE, MOD_CHANNEL


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
async def genocide(server_members):
    print(server_members)
    return

