import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

target_pattern = r"z+o+n*'?t*\s*(?:z+o+\s+i*t*)?|z+o+\s+i*t*"
counter = 0

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}\n")

@bot.event
async def on_message(message):
    global counter
    if message.author == bot.user:
        return

    if re.search(target_pattern, message.content.lower(), re.IGNORECASE):
        counter += 1
        await message.channel.send(f"Zon't Counter: {counter}")

    await bot.process_commands(message)

load_dotenv()
bot.run(os.getenv("TOKEN"))