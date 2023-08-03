import discord
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "ping", aliases = ["latency"])
    async def ping_command(self, ctx):
        embed = discord.Embed(title = "Pong!", description = f"Latency: {round(self.client.latency * 1000)}ms", color = 0x00ff00)
        await ctx.send(embed = embed)
    
async def setup(client):
    await client.add_cog(PingCommand(client))