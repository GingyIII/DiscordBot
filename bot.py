import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random


load_dotenv()



client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is connected to Discord!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)







