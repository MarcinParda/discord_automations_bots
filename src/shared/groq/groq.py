import os
from groq import Groq
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def generate_groq_response(
    prompt: str,
    conversation: List[Dict[str, str]]
) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful Discord assistant"},
                *conversation,
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content or "I'm sorry, I don't understand that"
    except Exception as e:
        return f"Error generating response: {str(e)}"
