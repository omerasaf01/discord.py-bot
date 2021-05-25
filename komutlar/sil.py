import discord
from discord.ext import commands

class Moderasyon(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name = "sil"
		)

	async def sil(self, ctx, arg = 1):
		if arg == 1:
			embed = discord.Embed(
				title = "Hata",
				description = "Minimum 1 Mesaj Silebilirim",
				color = 0x3598db
				)
			await ctx.send(embed = embed)
		else:
			await ctx.purge(limit = arg)
			embed = discord.Embed(
				title = "Başarılı!",
				description = arg + " Adet Mesaj Silindi",
				color = 0x3598db
				)
			await ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(Moderasyon(bot))
"""Altyapı Codexplant Tarafından Hazırlanmıştır"""