import os
from dotenv import load_dotenv
from walle.walle import Walle

if __name__ == "__main__":
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    if not DISCORD_TOKEN:
        raise ValueError(
            "DISCORD_TOKEN not found. Please set the DISCORD_DISCORD_TOKEN environment variable.")

    walle = Walle()
    walle.run(DISCORD_TOKEN)
