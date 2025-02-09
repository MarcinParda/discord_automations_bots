import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from walle.cogs.guild.message import MessageEvents
from walle.cogs.interactions.slash_commands import SlashCommands
from walle.cogs.client.ready import ReadyCog

async def add_cogs(bot):
  await bot.add_cog(MessageEvents(bot))
  await bot.add_cog(SlashCommands(bot))
  await bot.add_cog(ReadyCog(bot))

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def setup_bot():
    await add_cogs(bot)
    await bot.start(os.getenv('DISCORD_TOKEN'))

def run_bot():
    asyncio.run(setup_bot())
