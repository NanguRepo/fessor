import discord
from discord.ext import commands
import functions.utils
import discord_slash
from discord_slash import cog_ext

class Badass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="badass", description="😎", guild_ids=functions.utils.servers, default_permission=True, permissions=functions.utils.slPerms("banned"))
    async def badass(self, ctx: discord_slash.SlashContext):
      await ctx.send('https://imgur.com/a/QqFEkrm')

def setup(bot):
    bot.add_cog(Badass(bot))
