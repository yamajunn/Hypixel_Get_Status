import discord
from discord import app_commands
from api_contact import bedwars_status

TOKEN = ""

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Logged in as hypixel status")
    await tree.sync()#スラッシュコマンドを同期
    print("command sync")

@tree.command(name="command",description="コマンドリストを表示")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("/command : コマンドリストを表示する\n/oumu [str] : strをオウム返し")

@tree.command(name="oumu",description="オウム返し")
async def test_command(interaction: discord.Interaction,text:str):
    await interaction.response.send_message(text)

@tree.command(name="bedwars",description="ベッドウォーズのステータス")
async def test_command(interaction: discord.Interaction,name:str):
    data = bedwars_status(name)
    await interaction.response.send_message(data)


client.run(TOKEN)