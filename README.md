# Discord Automations Bot

This project is a Discord bot built using `discord.py` that provides various automations and integrations with external services like OpenAI, Groq, and Notion.

## Features

- **Message Handling**: Responds to messages and commands in Discord.
- **Slash Commands**: Supports slash commands and syncs them with Discord.
- **Thread Management**: Creates and manages threads based on user interactions.
- **External Integrations**: Integrates with OpenAI, Groq, and Notion for enhanced functionalities.

## TODO

- [x] Implement poetry for dependency management
- [x] Introduce docker
- [x] Implement extentions and extentions reloading
- [ ] Add OpenRouter integration
- [ ] Command to create a new thread for AI chatting
- [ ] Disable AI chatting in channels, keep it only in threads
- [ ] Implement previewing newsletter by command (TOP 5 articles with description)
- [ ] Implement triggering creating newsletter by command

## Setup

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd discord_automations_bots
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python -m venv discord_automations_bots_venv
   source discord_automations_bots_venv/bin/activate  # On Windows use `discord_automations_bots_venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   - Copy [.env.example](http://_vscodecontentref_/15) to [.env](http://_vscodecontentref_/16) and fill in the required values.

5. **Run the bot**:
   ```sh
   python src/main.py
   ```

## Usage

- **Commands**: Use slash commands to interact with the bot.
- **Message Handling**: Write a message to trigger AI response.
- **Thread Management**: The bot will create and manage threads based on interactions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.
