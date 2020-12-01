import discord, base64
from discord.ext import commands, tasks

class UtilsCog(commands.Cog, name="Some general utils"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hex2ascii', description="Hex to ascii\nTakes a hex string 0x123456 and returns ascii")
    async def hex2ascii(self, ctx, target: str):
        try:
            if target[:2].lower() == '0x':
                await ctx.send(bytes.fromhex(target[2:]).decode('ASCII'))
            else:
                await ctx.send(bytes.fromhex(target).decode('ASCII'))
        except Exception as e:
            await ctx.send(str(e))

    @commands.command(name="b64", description="decode or encode strings with base64")
    async def b64(self, ctx, operation: str, message: str):
        if operation[:1].lower() == 'e':
            await ctx.send(str(base64.b64encode(message.encode('ASCII'))))
        elif operation[:1].lower() == 'd':
            await ctx.send(str(base64.b64decode(message)))





def setup(bot):
    bot.add_cog(UtilsCog(bot))

