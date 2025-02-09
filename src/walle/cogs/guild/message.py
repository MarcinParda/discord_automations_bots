from discord import ChannelType
from discord.ext import commands
from shared.databases.notion import get_feed_urls_from_notion
from shared.prompts.get_prompt_category_prompt import get_prompt_category_prompt
from shared.groq.groq import generate_groq_response
from shared.utils.threads import respond_with_thread, respond_in_thread

class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if message.content == "ping":
            await message.channel.send("pong")
            return
        

        # Get prompt category from Groq
        prompt_category = await generate_groq_response(
            get_prompt_category_prompt(message.content),
            []
        )

        if prompt_category == 'GET_FEEDS_URL':
            feeds = await get_feed_urls_from_notion()
            feeds_url = '\n'.join(f"{feed['title']}: {feed['url']}" for feed in feeds)
            await message.reply(feeds_url)
        else:
            # Check if message is in a thread
            is_thread_message = message.channel.type in (
                ChannelType.public_thread,
                ChannelType.private_thread,
                ChannelType.news_thread
            )
            if is_thread_message:
                await respond_in_thread(message, self.bot)
                return
            else:
                await respond_with_thread(message, self.bot)
                return