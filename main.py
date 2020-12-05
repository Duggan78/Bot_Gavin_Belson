import discord
import discord.client
from discord.ext import commands
import asyncio
import hypixel



client = commands.Bot(command_prefix='!')

API_KEYS = ['399ada7a-43ae-4363-a159-7d873f25fba7']
hypixel.setKeys(API_KEYS)
Player = hypixel.Player('UHCHighlights')


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
    await ctx.send("https://discord.gg/vnJqump")
#to do- Going to have users use a command !dm (user) (message) to quick dm people using Gavin Belson.
@client.command()
async def dm(ctx):
    await client

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

PlayerName = Player.getName()
PlayerRank = Player.getRank()
@client.command()
async def Stats(ctx):
    await ctx.send(PlayerRank)
client.run('NjA5MTk3NTI0NDc3MjgwMjcy.XUzNaA.e7oBJGqOv64GIKo0y_oiaPb0zG0')
