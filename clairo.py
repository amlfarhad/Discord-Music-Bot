import discord
from discord import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(music(client))


