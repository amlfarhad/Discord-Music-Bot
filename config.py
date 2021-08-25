import discord
from discord import commands
import clairo

cogs = [clairo]

for i in range(len(cogs)):
    cogs[i].setup()

client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

client.run("ODgwMTM2NTUyMjUxMDI3NDU2.YSZ5Cg.2wncIIGsoQQjNjWyB9KLs1ZrdP0") #this is not the real token
