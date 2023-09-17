# Know that if you want any of this to work you need to install these modules.
# To do that you need to go to the terminal/command line and write "pip install (module-name-here)".
import discord
from discord.ext import commands
import youtube_dl


# Replace "!" with your prefered prefix
client = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def help(ctx):
    embed = discord.Embed(title="-HELP-", description="HERE ARE ALL MY COMMANDS!", colour=discord.Color.purple())
    embed.add_field(name= "!help", value="shows this message", inline=False)
    embed.add_field(name= "!ping", value="shows latency", inline=False)
    embed.add_field(name= "!hi", value="you'll see :)", inline=False)
    embed.add_field(name= "!mc", value="If you didn't know, I am compatible with the MineCordBot Minecraft server plugin.", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(client.latency * 1000)}ms')

@client.command()
async def hi(ctx):
    username = ctx.author.name
    displayname = ctx.author.display_name
    await ctx.send('Hello, ' + displayname + ' !')
    # GREAT PYTHON TIP TO REMEMBER: display_name (display name) and name (username)

@client.command()
async def mc(ctx):
    await ctx.send('Use " !!help " to see the commands for Minecraft.')



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