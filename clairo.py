import discord
from discord import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.voice.author is None:
            await ctx.send("You're not in a voice channel")
        voice_channel = ctx.voice.author.channel
        if ctx.voice_client is None:
            await voice_channel.connect()


def setup(client):
    client.add_cog(music(client))



