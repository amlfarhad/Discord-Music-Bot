import discord
from discord.ext import commands
import clairo
from dotenv import load_dotenv
load_dotenv()

cogs = [clairo]

client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

if __name__ == '__main__':
    import config
    client.run(os.getenv("YOUR TOKEN"))
