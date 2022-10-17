# bot.py
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
#cool imports

#funny words and variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MY_GUILD = os.getenv('GUILD_ID')


#discord stuff
intents = discord.Intents.default() #discord.Intents(value=3072)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class DiscordBot(): # no --- this does not work yet ... im fixing it :))
    
    # state shared by each instance
    __shared_state = dict()
 
    # constructor method
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'GeeksforGeeks'
    
    async def users(self): #this is the problem
        client = discord.Client(intents=intents)
        guild=discord.Object(id=MY_GUILD)
        userList = []
        for guild in client.guilds:
            for member in guild.members:
                userList.append(str(member))
        
        #users = guild.users(MY_GUILD)
        #userList.append(str(users))
        self.users = str(userList)
        print(userList)

    def __str__(self):
        return self.users


discBot = DiscordBot()


#a slash command for the bot to say hi to you in his own way
@tree.command(name = "sayhi", description = "Command that says hello", guild=discord.Object(id=MY_GUILD))
async def hello(interaction: discord.Interaction):
    username = interaction.user.name
    await interaction.response.send_message(f'I know where you live {username}')

#tells you your grades ... will tell you your grades one beautiful day
@tree.command(name = "grade", description = "Command, that send you your latest grades", guild=discord.Object(id=MY_GUILD))
async def grade(interaction: discord.Interaction):
    username = interaction.user.name
    await interaction.response.send_message(f'Your last grades were : *enter data here*, {username}')

@client.event
#prints sender and channel on each message (spyware much?) (this isn't necesarry but it is fun)
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message by {username} on {channel}')
    
    if message.author == client.user:
        return

    #Useless :)
    if channel == "studium-cum":
        if user_message.lower() == "!are you there":
            await message.channel.send(f'yes, ive been watching you {username}')
            return

@client.event
#pings when the bot is ready and connected
async def on_ready():
    await tree.sync(guild=discord.Object(id=MY_GUILD))
    print('{0.user} has connected to Discord!'.format(client))


client.run(TOKEN)

print(discBot.users())