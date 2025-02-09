import os
from dotenv import load_dotenv
from walle.walle import Walle

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        raise ValueError(
            "Token not found. Please set the DISCORD_TOKEN environment variable.")

    walle = Walle()
    walle.run(TOKEN)
