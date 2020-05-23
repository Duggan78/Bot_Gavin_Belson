import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


# Going to add the main commands down here.
@bot.command()
async def test(ctx):
    await ctx.send('testing passed!')


client.run('')
