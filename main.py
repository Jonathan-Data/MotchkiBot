import discord
from discord.ext import commands
import random
import logging
from tweety import Twitter
import asyncio

# Token
token = 'MTI5NTEyMDE2Mjc4OTUyMzUyNw.GYZ1gv.FshLGWUCDvkmvacA27kpXZWLAzQCBY5zJm4VJA'

# Main
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)

# Logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

last_tweet_id = None  # Global variable to keep track of the last tweet ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await send_tweets()  # Call the async function to send tweets

async def send_tweets():
    global last_tweet_id  # Declare as global to modify the variable
    username = "h360728"
    password = "gf7j3P7behG3."
    
    app = Twitter("session")
    
    try:
        app.sign_in(username, password)
    except Exception as e:
        print(f"Login failed: {e}")
        return  # Exit the function if login fails
    
    target_username = "Motchkii"
    user = app.get_user_info(target_username)
    all_tweets = app.get_tweets(user)

    channel = bot.get_channel(1295141061794205707)  # Replace with your channel ID

    for tweet in all_tweets:
        try:
            # Check if the tweet is a standard tweet
            if hasattr(tweet, 'id'):
                tweet_id = tweet.id if isinstance(tweet.id, int) else int(tweet.id)  # Ensure tweet.id is an int
                if last_tweet_id is None or tweet_id > last_tweet_id:
                    last_tweet_id = tweet_id  # Update the last tweet ID
                    tweet_link = f"https://twitter.com/{tweet.author.username}/status/{tweet_id}"
                    print(f"Sending tweet link: {tweet_link}")
                    await channel.send(tweet_link)
                else:
                    print(f"Skipping already sent tweet ID: {tweet_id}")
            else:
                print(f"Skipping unsupported tweet type: {tweet}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Failed to send message: {e}")

@bot.command()  # Adds two numbers together
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()  # Dice
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

@bot.command()  # Repeats message
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel(1295135393422901338)
#     if channel is not None:
#        await channel.send(f"Welcome @{member.display_name} to Motchki's Discord server!")

bot.run(token)
