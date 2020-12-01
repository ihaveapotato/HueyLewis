import discord
from discord.ext import commands

import sys, traceback, os

from dotenv import load_dotenv
load_dotenv()

initial_extensions = [
    'cogs.owner',
    'cogs.utils',
]

bot = commands.Bot(command_prefix='.', description='Number 1 son')

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'{bot.user.name} Booted')
    print(f'Servers list {bot.guilds}')
    await bot.change_presence(activity=discord.Game(name='Number 1 son'))
    print(f'Bot is running.\n')
    print(f'Invite link for bot: {discord.utils.oauth_url(bot.user.id)}')

discordToken = os.getenv("discordToken")
bot.run(discordToken, bot=True, reconnect=True)

