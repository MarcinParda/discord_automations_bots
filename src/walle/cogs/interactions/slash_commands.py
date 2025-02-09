import discord
from discord import app_commands
from discord.ext import commands
from shared.databases.notion import get_feed_urls_from_notion

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clearchannel", description="Clears all messages in the channel")
    async def clear_channel(self, interaction: discord.Interaction):
        """Clear up to 100 messages and all threads in the channel."""
        await interaction.response.send_message("Clearing channel...")
        channel = interaction.channel
        async for message in channel.history(limit=100):
            await message.delete()
        for thread in channel.threads:
            async for message in thread.history(limit=100):
                await message.delete()

    @app_commands.command(name="getfeedurls", description="Shows feed URLs from Notion")
    async def get_feed_urls(self, interaction: discord.Interaction):
        """Fetch and display feed URLs from Notion."""
        feeds = await get_feed_urls_from_notion()
        message = "\n".join(f"{feed['title']}: {feed['url']}" for feed in feeds)
        await interaction.response.send_message(message)

def setup(bot: commands.Bot):
    bot.add_cog(SlashCommands(bot))