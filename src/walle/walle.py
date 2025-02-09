import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from walle.cogs.cogs import add_cogs

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def setup_bot():
    await add_cogs(bot)
    await bot.start(os.getenv('DISCORD_TOKEN'))

def run_bot():
    asyncio.run(setup_bot())
