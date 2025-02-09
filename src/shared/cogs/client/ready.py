from discord.ext import commands


class ReadyCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.setup_bot_commands()

    async def setup_bot_commands(self):
        """
        Set up and sync slash commands when the bot is ready.
        """
        print(f'Logged in as {self.bot.user.name}!')

        try:
            print('Started syncing application (/) commands.')
            await self.bot.tree.sync()
            print('Successfully synced application (/) commands.')
        except Exception as e:
            print(f'An error occurred while syncing commands: {e}')
