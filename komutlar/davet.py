import discord
from discord.ext import commands


class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(
		name = "davet"
		)

	async def davet(self, ctx):
		embed = discord.Embed(
			title = "Infinity | Davet",
			description = "[Davet](LİNK)\n[Destek Sunucum](LİNK)",
			color = 0x3598db
			)
		await ctx.send(embed = embed)


def setup(bot):
	bot.add_cog(Bot(bot))
"""Altyapı Codexplant Tarafından Hazırlanmıştır"""