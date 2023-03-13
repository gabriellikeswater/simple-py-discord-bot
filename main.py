import discord
from discord.ext import commands

# Replace 'YOUR_TOKEN_HERE' with your bot's token
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(client.latency * 1000)}ms')

@client.command()
async def hi(ctx):
    await ctx.send('hello, {user}!')

@client.command()
async def cmds(ctx):
    await ctx.send('Here are the available commands: !ping, !hi')

client.run('MTA0NjE5NTczOTUzMDkwNzc0OA.Ga3f6b.FhghK2YYi_Z63wEDXtTFE1IPAiNG4ynpTkDySg')