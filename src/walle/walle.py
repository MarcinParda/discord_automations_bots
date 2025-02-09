import discord
from discord.ext import commands
from shared.cogs.client.ready import ReadyCog
from walle.cogs.guild.message import MessageCog
from walle.cogs.interactions.commands import CommandsCog


class Walle(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='/', intents=intents)

    async def setup_hook(self):
        await self.add_cog(MessageCog(self))
        await self.add_cog(CommandsCog(self))
        await self.add_cog(ReadyCog(self))
