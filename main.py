import discord
from discord.ext import commands
import music
import basic

cogs = [music, basic]

client = commands.Bot(command_prefix='/', intents=discord.Intents.all(), help_command=None)

for i in range(len(cogs)):
    cogs[i].setup(client)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='pas du tout de la musique'))
    print("I'm ready !")

client.run("TOKEN")