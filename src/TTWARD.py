# bot.py
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import asyncio
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
MY_GUILD = os.getenv('GUILD_ID')
BOT_CHANNEL = os.getenv("DISCORD_CHANNEL_ID")
intents = discord.Intents.default() #discord.Intents(value=3072)
guild=discord.Object(id=MY_GUILD)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

gradeText = str()

async def appiArgoAnnabPeksa(appi):
    global BOT_CHANNEL
    print(BOT_CHANNEL)
    channel = client.get_channel(BOT_CHANNEL)
    await channel.send(appi)


@client.event
#pings when the bot is ready and connected
async def on_ready():
    # print("ready")
    global gradeText
    global BOT_CHANNEL
    await tree.sync(guild=discord.Object(id=MY_GUILD))
    print('{0.user} has connected to Discord!'.format(client))
    channel = client.get_channel(int(BOT_CHANNEL))
    # print(BOT_CHANNEL)
    # print(channel)
    await channel.send(gradeText)
    await client.close()
    return

def runBot(string) -> None:
    global intents
    global client
    global TOKEN
    client = discord.Client(intents=intents)
    global gradeText
    gradeText = string
    asyncio.run(client.start(TOKEN))

# runBot("I")
def sendMessage(string):
    print("elo tim", TOKEN, BOT_CHANNEL)
    global gradeText
    gradeText = string
    client = discord.Client(intents=intents)
    asyncio.run(client.start(TOKEN))

file = open("./src/gradeText.txt", encoding="UTF-8")
gradeText = file.read()
file.close()

client.run(TOKEN)
