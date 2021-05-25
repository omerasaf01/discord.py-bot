import discord
from discord.ext import commands

class Moderasyon(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.command(
		name = "deneme"
		)

	async def deneme(self, ctx):
		embed = discord.Embed(
			title = "Başlık",
			description = "AÇIKLAMA",
			color = 0x3598db
			)
		ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(Moderasyon(bot))

"""Altyapı Codexplant Tarafından Hazırlanmıştır"""