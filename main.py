import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_ready():
    print("The bot works")
    print("------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I work.")

client.run('MTI5NTEyMDE2Mjc4OTUyMzUyNw.Gj66Wl.kgf7m1t3bQcxpnCZj57-6iPY0yO76enhCBhCXk')
