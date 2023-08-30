# JARVIS Discord Bot developed by Navneet Kishan Srinivasan


import discord
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        #print(message.mentions)
        if self.user != message.author:
            if self.user in message.mentions:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.content,
                    temperature=1.0,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                messageToSend = response.choices[0].text
                await message.channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
