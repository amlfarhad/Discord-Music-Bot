import discord
from discord import commands
import clairo

cogs = [clairo]

client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

token = 'ODgwMTM2NTUyMjUxMDI3NDU2.YSZ5Cg.RxxF5qFbYCgaWoNObQTAfjWG1Ss'
