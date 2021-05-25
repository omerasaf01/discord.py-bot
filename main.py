"""Altyapı Codexplant Tarafından Hazırlanmıştır"""
import os
import discord
from discord.ext import commands

#-----------------------------------------

Prefix = "s!"

Token = "TOKENİNİZ"

#-----------------------------------------

Bot = commands.Bot(command_prefix = Prefix)

@Bot.event
async def on_ready():
    print("Bot Aktif")
    aktivite = discord.Game(name = "Deneme", type = 3)
    await Bot.change_presence(activity=discord.Game(name="Ömer Asaf Karasu#3842"))

@Bot.command()
async def load(self, ctx):
    if ctx.message.author == 752243590985678878:
        for filename in os.listdir("komutlar"):
            if filename.endswith(".py"):
                Bot.laod_extension(f"komutlar.{filename[:-3]}")

for filename in os.listdir("komutlar"):
    if filename.endswith(".py"):
        Bot.load_extension(f"komutlar.{filename[:-3]}")
        print(filename)




Bot.run(Token)

"""Altyapı Codexplant Tarafından Hazırlanmıştır"""