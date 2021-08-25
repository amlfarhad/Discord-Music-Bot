import discord
from discord.ext import commands
import clairo



cogs = [clairo]

client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

if __name__ == '__main__':
    import config
    client.run(config.token)
