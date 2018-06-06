##Rework for SSN Discord Bot

# Imports for bot
import discord
from discord import opus
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
# Finished of Imports


#Command Prefix for bot
bot = commands.Bot(command_prefix= ".")
OPUS_LIBS = ['libopus0']

async def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

#Sends this to Python CMD when bot is ready!
@bot.event
async def on_ready():
    print("Get ready to rev up those fryers!")
    print("I am running on" + bot.user.name)

# When the command ping is sent then the outpout will contain ":ping_pong: Pong!"
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.send_message(ctx.message.channel, ":ping_pong: Pong!")


def time_o():
    import time
    if("00" <= time.strftime("%M") <= "29"):
        return ''
    elif("30" <= time.strftime("%M") <= "59"):
        return "30"

# When the command time is sent then the output will contain the system time plus EDT timezone and a clock emoji
@bot.command(pass_context=True)
async def time(ctx):
    import time
    raw_time = time.strftime("%I%M")
    hour = time.strftime("%I")
    local_time = time.strftime("%I:%M")
    await bot.send_message(ctx.message.channel, "It's {} EDT :clock{}{}:".format(local_time, hour, time_o()))
# When command is sent it will check if the role "Daddy" is current in the sender
# When command info is sent it will display info about the user
@bot.command(pass_context=True)
@commands.has_role("Daddy")
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Information you can use against them :wink:", color=0x33FFD2)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Top Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(ctx.message.channel, embed=embed)
    await bot.delete_message(ctx.message)

#When command kick is sent it will kick the user mentioned unless the sender does not have the right permission.
@bot.command(pass_context=True)
@commands.has_role("Daddy")
async def kick(ctx, user: discord.Member):
    await bot.send_message(ctx.message.channel, ":boot: :ear_of_rice: Not in my, {} ricefields! :ear_of_rice: :boot:".format(user.mention) )
    await bot.kick(user)
    await bot.delete_message(ctx.message)

#When command fred is sent it will do the fred says fuck meme.
@bot.command(pass_context=True)
async def fred(ctx):
    await bot.send_message(ctx.message.channel, "Scooby says 'Ruh Roh!'")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "Shaggy says 'Zoinks!'")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "Velma says 'Jinkies!'")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "Daphne says 'Jeepers!'")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "What does Fred say?")
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, "Fred says 'Fuck.'")
    await bot.send_message(ctx.message.channel, "No he DOES NOT!")
    await bot.delete_message(ctx.message)

@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    server = message.server
    mention = message.author.mention
    if message.content.startswith("no u"):
        if(message.author.bot):
            print("{}: {} {}: {}".format(server, channel, author, content))
            await bot.process_commands(message)

        else:
            print("{}: {} {}: {}".format(server, channel, author, content))
            await bot.send_message(channel, "no u {}".format(mention))
            await bot.process_commands(message)

    elif(message.author.bot):
        print("{}: {} {}: {}".format(server, channel, author, content))
        await bot.process_commands(message)

    else:
        print("{}: {} {}: {}".format(server, channel, author, content))
        await bot.process_commands(message)

@bot.command(pass_context=True)
async def brent(ctx):
    voice_channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(voice_channel)
    voice.play(discord.FFmpegPCMAudio('./That_Time.mp3'))



# TOKEN FOR BOT
bot.run("NDQ3NDcxOTkyNDAxMjk3NDE4.DeIH9w.2O8b11UIDMCvAX8qKutMiBtH1KQ")
