import discord
from discord.ext import commands
import youtube_dl

# Replace "!" with your prefered prefix
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
async def play(ctx, url: str):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("You must be in a voice channel to play music!")
        return
    vc = await voice_channel.connect()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': False,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        player = await vc.play(URL)
        await ctx.send(f"Music playing: {info['title']}")

@client.command()
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()

@client.command()
async def disconnect(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Bot disconnected from voice channel.")

# Replace "YOUR-BOT-TOKEN-GOES-HERE" with your bot's token - Keep the ''''''''s, ok?
client.run('YOUR-BOT-TOKEN-GOES-HERE')
