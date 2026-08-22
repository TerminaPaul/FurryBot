from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands

load_dotenv("TOKEN.env")
TOKEN = getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"awdwadawdawd caillou {bot.user}")

bot.run(TOKEN)