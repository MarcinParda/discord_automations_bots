import discord
from discord import Client
from discord.ext import commands
import asyncio
from typing import List, Dict
from shared.groq.groq import generate_groq_response
from shared.prompts.generate_thread_name import generate_thread_name
from shared.constants.discord import MAX_MESSAGE_CHAR_LENGTH
from shared.utils.message import split_message_into_chunks

async def respond_with_thread(message: discord.Message, client: Client) -> None:
    try:
        async with message.channel.typing():
            # Remove bot mention from prompt
            prompt = message.content.replace(f'<@{client.user.id}>', '').strip()
            
            # Concurrently generate response and thread name
            response, thread_name = await asyncio.gather(
                generate_groq_response(prompt, []),
                generate_groq_response(generate_thread_name(prompt), [])
            )
            
            # Create thread and send response
            thread = await message.create_thread(
                name=thread_name[:100],  # Ensure name length <= 100 chars
                auto_archive_duration=60
            )
            await thread.send(response)
            
    except Exception as e:
        print(f'Error in respond_with_thread: {e}')
        await message.reply('An error occurred while creating the thread response')


async def respond_in_thread(message: discord.Message, client: commands.Bot) -> None:
    try:
        async with message.channel.typing():
            messages = [msg async for msg in message.channel.history(limit=None)]
            
            conversation: List[Dict[str, str]] = []
            for msg in reversed(messages):
                if msg.author == client.user:
                    conversation.append({"role": "assistant", "content": msg.content})
                else:
                    conversation.append({"role": "user", "content": msg.content})

            response = await generate_groq_response(message.content, conversation)
            response_chunks = split_message_into_chunks(response, MAX_MESSAGE_CHAR_LENGTH)

            for chunk in response_chunks:
                await message.reply(chunk)
    except Exception as error:
        print(f"Error: {error}")
        await message.reply("An error occurred while processing your request")