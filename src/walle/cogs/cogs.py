from walle.cogs.guild.message import MessageEvents
from walle.cogs.interactions.slash_commands import SlashCommands
from walle.cogs.client.ready import ReadyCog

async def add_cogs(bot):
  await bot.add_cog(MessageEvents(bot))
  await bot.add_cog(SlashCommands(bot))
  await bot.add_cog(ReadyCog(bot))