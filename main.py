# main
import discord
from discord.ext import commands
import random
# logging
import logging
# Tweety
from tweety import Twitter

# Token
token = 'MTI5NTEyMDE2Mjc4OTUyMzUyNw.Gj66Wl.kgf7m1t3bQcxpnCZj57-6iPY0yO76enhCBhCXk'
# main
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)
# Logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Server sided

@bot.command() # Adds two numbers together
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command() # Dice
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command() # Repeats message
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1295135393422901338)  
    if channel is not None:  
        await channel.send(f"Welcome @{member.display_name} to Motchki's Discord server!")

#Tweety
#username = ""
#password = ""
#app = Twitter("session")
#app.sign_in(username, password)
#target_username = "motchkii"

#user = app.get_user_info(target_username)
#all_tweets = app.get_tweets(user)

#for tweet in all_tweets:
#    channel = bot.get_channel("1295141061794205707")
#    channel.send(tweet)

bot.run(token, log_handler=handler)