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



@client.command()
async def guess(ctx, max:int=2):
    num = random.randint(1,max)
    attempts = 5
    await ctx.send(f'Guessing game started!\nPlease guess a number between **1-{max}**')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.message.channel
    while attempts >= 0:
        guess = await client.wait_for('message', check=check)
        if guess.content == str(num):
            await ctx.send('You guessed correctly!')
            attempts = 0
        else:
            await ctx.send(f'Whoops... try again. You have **{attempts}** more attempts')
            attempts -= 1

        




TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)







