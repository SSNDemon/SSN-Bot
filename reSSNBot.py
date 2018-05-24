##Rework for SSN Discord Bot

# Imports for bot
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
# Finished of Imports

#Command Prefix for bot
bot = commands.Bot(command_prefix= ".")

#Sends this to Python CMD when bot is ready!
@bot.event
async def on_ready():
    print("Get ready to rev up those fryers!")
    print("I am running on" + bot.user.name)

# When the command ping is sent then the outpout will contain ":ping_pong: Pong!"
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.send_message(ctx.message.channel, ":ping_pong: Pong!")

# When the command time is sent then the output will contain the system time plus EDT timezone and a clock emoji
@bot.command(pass_context=True)
async def time(ctx):
    import time
    raw_time = time.strftime("%I%M")
    local_time = time.strftime("%I:%M")
    channel = ctx.message.channel
    print(raw_time)
    if("1159" < raw_time < "1229"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock12:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock1230:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock1:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock130:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock2:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock230:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock3:")
    elif("1230" < raw_time < "1259"):
        await bot.send_message(channel, "It's " + localtime + "EDT :clock330:")
    else:
        await bot.send_message(channel, "It's" + localtime + "EDT")

# When command is sent it will check if the role "Daddy" is current in the sender
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



# TOKEN FOR BOT
bot.run("NDQ3NDcxOTkyNDAxMjk3NDE4.DeIH9w.2O8b11UIDMCvAX8qKutMiBtH1KQ")