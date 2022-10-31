# bot.py
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
MY_GUILD = os.getenv('GUILD_ID')
BOT_CHANNEL = os.getenv("CHANNEL_ID")
intents = discord.Intents.default() #discord.Intents(value=3072)
guild=discord.Object(id=MY_GUILD)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
    
async def appiArgoAnnabPeksa(appi):
    global BOT_CHANNEL
    channel = client.get_channel(id=BOT_CHANNEL)
    await channel.send(appi)


@client.event
#pings when the bot is ready and connected
async def on_ready():
    await tree.sync(guild=discord.Object(id=MY_GUILD))
    print('{0.user} has connected to Discord!'.format(client))

async def run() -> None:
    client.run(TOKEN)
