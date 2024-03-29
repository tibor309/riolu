import discord
import os
from discord.ext import commands
from config import bot_token, bot_time

#from keep_alive import keep_alive # Flask server to make the bot run 24/7 (uncomment if you're on replit or similar)

intents = discord.Intents.default()
bot = commands.Bot(intents=intents, help_command=None)


# Load commands
for f in os.listdir("./commands"):
    if f.endswith(".py"):
        try:
            bot.load_extension("commands." + f[:-3]) # commands
        except Exception as error:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"ERROR {f} could not be loaded: {error}")
        else:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded {f}")

@bot.event
async def on_ready():
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"Logged in as {bot.user}")

# Make bot not respond to it's owm messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


#keep_alive() # uncomment this too

try:
  bot.run(bot_token)
except discord.HTTPException as err:
    if err.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise err