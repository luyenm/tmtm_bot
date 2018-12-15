from discord.utils import get
from Administration.channel_data import AUTHORIZED_SERVER
import random


async def get_text(message, client):

    if message.server.id == AUTHORIZED_SERVER:
        if 'stem major btw' in str(message.content.lower()):
            emoji_id = get(client.get_all_emojis(), name='gachiGASM')
            await client.add_reaction(message, emoji_id)

    if '┻━┻' in str(message.content.lower()):
        responses = [
            "┬─┬ノ( º _ ºノ) now now...",
            "┬─┬ノ( º _ ºノ) no need for anger...",
            "┬─┬ノ( º _ ºノ) please, settle down...",
            "┬─┬ノ( º _ ºノ) we're adults here...",
            "┬─┬ノ( º _ ºノ) have some tea dear..."
        ]
        await client.add_reaction(message, '🍵')
        await client.send_message(message.channel, responses[random.randint(0, len(responses))])

    if client.user in message.mentions:
        emoji_id = get(client.get_all_emojis(), name='YAMERO')
        await client.add_reaction(message, emoji_id)
