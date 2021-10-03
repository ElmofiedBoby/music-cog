import discord
from discord.ext import commands
import config


bot = commands.Bot(command_prefix='!', description="nithin\'s personal music/fun bot")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    activity = discord.Game(name='your mom')
    await bot.change_presence(activity=activity)

@bot.event
async def on_reaction_add(reaction, user):
    quotes = bot.get_channel(888832318511386644)
    if user.bot:
        return
    if reaction.emoji == '\U0001F4F8':
        await quotes.send("\"{0}\" -{1}".format(reaction.message.content, reaction.message.author))

bot.load_extension('cogs.music_queue')
bot.load_extension('cogs.chat')

bot.run(config.token)

