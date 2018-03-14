import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Sending messages via console", url="https://twitch.tv/streamer", type=1))
    server=input('Server ID: ')
    ch=input('Channel ID: ')
    print('Enjoy sending messages!')
    print('-----------------------')
    while True:
        msg=input()
        server = client.get_server(server)
        await client.send_message(client.get_channel(ch), msg)
		
client.run("YOUR TOKEN HERE")