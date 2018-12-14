from discord.utils import get
from Administrative.channel_data import AUTHORIZED_SERVER


async def get_text(message, client):

    if message.server.id == AUTHORIZED_SERVER:
        if 'stem major btw' in str(message.content.lower()):
            emoji_id = get(client.get_all_emojis(), name='gachiGASM')
            await client.add_reaction(message, emoji_id)
