"MTE1NzMwNTQ0Mzc1Mjg3ODEyMQ.GRoow3.0oKWRN7kSCXC9FG6jPyCo-qf6Dr3kho-NFKHAI"

import discord
from discord import app_commands

TOKEN = "MTE1NzMwNTQ0Mzc1Mjg3ODEyMQ.GRoow3.0oKWRN7kSCXC9FG6jPyCo-qf6Dr3kho-NFKHAI"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

source_channel_id = 1087027349142384701
destination_channel_id = 865770071603281940

@client.event
async def on_ready():
    print("Logged in as Color Bot")
    await tree.sync()
    print("command sync")

@tree.command(name="oumu",description="オウム返し")
async def test_command(interaction: discord.Interaction,text:str):
    await interaction.response.send_message(text)

@client.event
async def on_message(message):
    # コピー元のチャンネルからのメッセージだけをコピー先のチャンネルに送信
    if message.channel.id == source_channel_id:
        destination_channel = client.get_channel(destination_channel_id)

        await destination_channel.send(message.content)

client.run(TOKEN)