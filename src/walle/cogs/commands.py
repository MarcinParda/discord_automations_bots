import discord
from discord import app_commands
from discord.ext import commands
from shared.databases.notion import get_feed_urls_from_notion


class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="purgechannel", description="Purge channel")
    async def purge_channel(self, interaction: discord.Interaction):
        if not isinstance(interaction.channel, discord.TextChannel):
            await interaction.response.send_message("This command can only be used in text channels.")
            return

        await interaction.channel.delete()
        new_channel = await interaction.channel.clone(reason="Channel was purged")
        await new_channel.edit(position=interaction.channel.position)
        await new_channel.send("Channel was purged")

    @app_commands.command(name="getfeedurls", description="Shows feed URLs from Notion")
    async def get_feed_urls(self, interaction: discord.Interaction):
        """Fetch and display feed URLs from Notion."""
        feeds = await get_feed_urls_from_notion()
        message = "\n".join(
            f"{feed['title']}: {feed['url']}" for feed in feeds)
        await interaction.response.send_message(message)

    @app_commands.command(name="reloadallextentions", description="Reload all extentions of the bot")
    async def reload_all_extentions(self, interaction: discord.Interaction):
        """Reloads all active extensions"""
        extensions = list(self.bot.extensions.keys())
        
        for ext in extensions:
            try:
                await self.bot.reload_extension(ext)
            except commands.ExtensionError as e:
                print(f"❌ {ext}: {e}")
                return
        
        await interaction.response.send_message(f"🔄 Reloaded {len(extensions)} extensions")


async def setup(bot):
    await bot.add_cog(CommandsCog(bot))