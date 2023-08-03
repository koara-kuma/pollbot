import discord
from discord.ext import commands
import asyncio

class PollCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="poll")
    async def poll_command(self, ctx, *, message: str):
        # Split the message by "|" to separate the question and emojis
        parts = message.split("|")
        if len(parts) < 3:
            return await ctx.send("Please provide a question and at least two emojis separated by '|'. example wokpoll What is your favorite color? | :red_circle: | :blue_circle: | :green_circle:")

        question = parts[0].strip()
        emojis = [emoji.strip() for emoji in parts[1:]]

        if len(emojis) < 2:
            return await ctx.send("Please provide at least two emojis for the poll.")

        embed = discord.Embed(title=f"Survey Created by {ctx.author.mention}", description=question, color=0x00ff00)
        poll_message = await ctx.send(embed=embed)

        for emoji in emojis:
            await poll_message.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == poll_message.id and str(reaction.emoji) in emojis

        try:
            reaction, _ = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
            await ctx.send(f"{ctx.author.mention} voted: {reaction.emoji}")
        except asyncio.TimeoutError:
            await ctx.send("The poll has ended, no one voted.")

async def setup(client):
    await client.add_cog(PollCommand(client))
