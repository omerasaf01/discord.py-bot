import discord
from discord.ext import commands

class Yapimci(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name = "yapimci"
		)

	async def yapimci(self, ctx):
		embed = discord.Embed(
			title = "Yapımcım",
			description = "Bu ALtyapı Codexplant Tarafından Hazırlanmıştır![Destek Sunucumuz](httpd://shop.codexplant.xyz)",
			color = 0x3598db

			)
		ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(Yapimci(bot))

""" Altyapı CODEXPLANT TARAFINDAN YAPILMIŞTIR!"""