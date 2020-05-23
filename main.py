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


client.run('')
