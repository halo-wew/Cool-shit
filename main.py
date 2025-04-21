from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

# Flask web server
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True  # Needed for !hello
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hi! I’m alive on Replit.")

# Start server and bot
keep_alive()
bot.run(os.getenv("TOKEN"))