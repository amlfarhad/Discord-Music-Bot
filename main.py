import discord
from discord.ext import commands
import clairo
import os

my_secret = os.environ['token']

cogs = [clairo]

client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(my_secret)
