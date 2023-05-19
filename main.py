import discord
from harrito_utils import process_msg, sense_init
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER = os.getenv('BOT_OWNER_ID')

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
sense_init()

client.run(TOKEN)

