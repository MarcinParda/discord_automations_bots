import pathlib
import discord
from discord.ext import commands


class Walle(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='/', intents=intents)

    async def load_extensions_from_path(self, path, prefix):
        for file in path.glob('*.py'):
            if file.name == '__init__.py':
                continue
            if file.name.endswith('.py'):
                await self.load_extension(f'{prefix}.{file.name[:-3]}')

    async def setup_hook(self):
        walle_cogs_path = pathlib.Path('walle/cogs')
        shared_cogs_path = pathlib.Path('shared/cogs')

        await self.load_extensions_from_path(walle_cogs_path, 'walle.cogs')
        await self.load_extensions_from_path(shared_cogs_path, 'shared.cogs')