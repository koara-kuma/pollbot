import discord
from discord.ext import commands
import json
import os
import asyncio

if os.path.exists(os.getcwd() +"/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {'Token': ""}
    
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

help_command = commands.DefaultHelpCommand(
    hello_category = "Say hello to miloceo :)",
    ping_category = "Check the bot's latency",
    quote_category = "Quote a message",
    no_category = "Help"
)

client = commands.Bot(command_prefix = 'wok', help_command = help_command, intents= discord.Intents.all())

@client.event
async def on_ready():
    activity = discord.Game(name=f"in {len(client.guilds)} servers | wokhelp", type=1)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    embed = discord.Embed(title = f'Welcome to {member.guild.name}!')
    embed.colour = discord.Colour.orange()
    embed.description = f'Welcome {member.mention} to {member.guild.name} hope you enjoy your stay and remember to follow the rules :heart:'
    await member.send(embed=embed)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename}")

token = configData['Token']

async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())

