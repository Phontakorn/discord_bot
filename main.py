import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

#จะให้สนใจในเหตุการณ์ไหน
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print("Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} commands")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1380219586410053732) #ID channel
    text = f"Welcome : {member.mention}!"
    emmbed = discord.embed(title = 'Welcome to server!',
                           description = text,
                           color = 0xFFBDC2)

    await channel.send(embed = emmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1380219586410053732) #ID channel
    text = f"Goodbye : {member.mention}!"
    emmbed = discord.embed(title = 'Goodbye T^T',
                           description = text,
                           color = 0xFFBDC2)

    await channel.send(embed = emmbed)

@bot.tree.command(name='testhello', description='Show text hello')
async def testhello(interaction):
    await interaction.response.send_message('Hello Testing!')

@bot.tree.command(name='name')
@app_commands.describe(name ="What's your name?")
async def sendname(interaction: discord.Interaction, name: str):
    embed = discord.Embed(
        title=f"Welcome : {name}",
        color=0xFFBDC2,
        timestamp=discord.utils.utcnow()
    )

    await interaction.response.send_message(embed=embed)

    # ดึง member จาก interaction.user
    member = interaction.user
    if isinstance(member, discord.Member):
        role = interaction.guild.get_role(1380243560594673684)
        if role:
            await member.add_roles(role)
server_on()
bot.run(os.getenv('TOKEN'))
