# JARVIS - AI Discord Bot

JARVIS is a Python 3-based chatbot developed by Navneet Kishan Srinivasan that integrates the Discord's API with OpenAI's language model. This chatbot listens to messages in a Discord server and generates responses using OpenAI's text-davinci-003 model.

## Technologies Used
- **Discord.py**: The bot is built using the discord.py library, enabling interaction with the Discord API.
- **OpenAI API**: OpenAI's API is utilized to generate contextual and coherent responses to user messages.
- **Python 3.x**: The script is written in Python 3.x, ensuring compatibility and readability.
- **Environment Variables**: The bot uses environment variables to securely store sensitive data like API keys.

## Features
- Listens to messages/questions in a Discord server and responds when mentioned.
- Integrates OpenAI's text-davinci-003 model to generate meaningful and contextually relevant responses.
- Customizable response generation parameters including temperature, max tokens, top p, frequency penalty, and presence penalty.

## Usage
To deploy and interact with the DiscordOpenAIChatBot, follow these steps:

1. **Create Bot**: Go to the Discord Developer Portal and create a bot. Get the bot's token.
2. **Get API Key**: Get an API key from OpenAI and keep it secure.
3. **Set Keys**: Set the OpenAI key as OPENAI_API_KEY and the bot token as SECRET_KEY in your system's environment variables.
4. **Customize (Optional)**: If required the token size, temperature, frequency penalty and other parameters can be changed to suit the users' needs.
5. **Run Script:** Run the provided Python script.
6. **Mention the bot by using @JARVIS and post your message/question.**
## Note
This project serves as a starting point for integrating Discord and OpenAI. Feel free to expand and refine the functionality to align with your specific use cases.

## Dependencies
- Python 3.x
- discord.py library
- openai library
![JARVIS_profile](https://github.com/NavneetKishanS/JARVIS_DiscordBot/assets/115086283/14c024b5-9da8-433f-8658-dbd52321abe5)
