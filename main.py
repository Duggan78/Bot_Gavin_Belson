import discord
import discord.client
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Going to add the main commands down here.
@client.command()
async def shutdown(ctx):
    await client.close()
    print("the client has disconnected itself")


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
# Clear command stolen from github.com/baconman322... Thank You! haha

@client.command()
async def invitelink(ctx):
    await ctx.send("https://discord.gg/cvWBwj")

@client.command()
async def ErhlichBachman(ctx):
    await ctx.send("JINNNNN-YANNNNGGGGG!!!!!!!")

@client.command()
async def Gilfoyle(ctx):
    await ctx.send("Makes me feel like I’ve died and gone to hell.")

@client.command()
async def Gilfoyle2(ctx):
    await ctx.send("I’m sure you can find your way out with one of your two faces.")

@client.command()
async def Gilfoyle3(ctx):
    await ctx.send("I’m effectively leveraging your misery. I’m like the Warren Buffet of f*cking with you.")



client.run('')
