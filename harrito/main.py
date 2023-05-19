import discord
import os
from dotenv import load_dotenv
import sys

from interface.hardware import *
from frames.command import Command

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER = os.getenv('BOT_OWNER_ID')


async def process_msg(message):
    comm = Command(message)
    response = await comm.resolve()
    col = (255, 255, 255)
    if (response.error):
        response.message = "ERROR: " + response.message
        col = (255, 0, 0)

    await comm.message.channel.send(response.message)
    if (response.display):
        display_message(response.message, col)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        if str(message.channel.type) != 'private':
            return
        
        if (message.author.id != int(OWNER)):
            return
        
        await process_msg(message)

client = MyClient(intents=discord.Intents.default())
hardware_init()

client.run(TOKEN)

