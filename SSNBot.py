# SSN Bot
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time


#Command Prefix for the bot
bot = commands.Bot(command_prefix='!!')
client = discord.Client()
#Displays stuff on CMD of program bot
@bot.event
async def on_ready():
    print ("Get ready to rev up those fryers!")
    print ("I am running on" + bot.user.name)

#Pings the bot with (command_prefix)ping
@bot.command(pass_context=True)
async def ping(ctx):
    await  ctx.send(":ping_pong: pong!!")
#Time command to display bot
@bot.command(pass_context=True)
async def time(ctx):
    import time
    timeL = time.strftime("%I%M")
    localtime = time.strftime("%I:%M %p")
    if(timeL == "0420"):
        await ctx.send("It's 4:20 EDT :clock4: Wooo!  <:blunt:447646223587999765>  <:weed:447646187214864385>")
    elif("0400" <= timeL <= "0429"):
        await ctx.send(localtime + " EDT :clock4:")
    elif("0430" <= timeL <= "0459"):
        await ctx.send(localtime + " EDT :clock430:")
    elif( "0500" <= timeL <= "0529"):
        await ctx.send(localtime + " EDT :clock5:")
    elif("0530" <= timeL <= "0559"):
        await ctx.send(localtime + " EDT :clock530:")
    elif("0600" <= timeL <= "0629"):
        await ctx.send(localtime + " EDT :clock6:")
    elif("0630" <= timeL <= "0659"):
        await ctx.send(localtime + " EDT :clock630:")
    elif("0700" <= timeL <= "0729"):
        await ctx.send(localtime + " EDT :clock7:")
    elif("0730" <= timeL <= "0759"):
        await ctx.send(localtime + " EDT :clock730:")
    elif("0800" <= timeL <= "0829"):
        await ctx.send(localtime + " EDT :clock8:")
    elif("0830" <= timeL <= "0859"):
        await ctx.send(localtime + " EDT :clock830:")
    elif("0900" <= timeL <= "0929"):
        await ctx.send(localtime + " EDT :clock9:")
    elif("0930" <= timeL <= "0959"):
        await ctx.send(localtime + " EDT :clock930:")
    elif("1000" <= timeL <= "1029"):
        await ctx.send(localtime + " EDT :clock10:")
    elif("1030" <= timeL <= "1059"):
        await ctx.send(localtime + " EDT :clock1030:")
    elif("1100" <= timeL <= "1129"):
        await ctx.send(localtime + " EDT :clock11:")
    elif("1130" <= timeL <= "1159"):
        await ctx.send(localtime + " EDT :clock1130:")
    elif("1200" <= timeL <= "1229"):
        await ctx.send(localtime + " EDT :clock12:")
    elif("1230" <= timeL <= "1259"):
        await ctx.send(localtime + " EDT :clock1230:")
    elif("0100" <= timeL <= "0129"):
        await ctx.send(localtime + " EDT :clock1:")
    elif("0130" <= timeL <= "0159"):
        await ctx.send(localtime + " EDT :clock130:")
    elif("0200" <= timeL <= "0229"):
        await ctx.send(localtime + " EDT :clock2:")
    elif("0230" <= timeL <= "0259"):
        await ctx.send(localtime + " EDT :clock230:")
    elif("0300" <= timeL <= "0329"):
        await ctx.send(localtime + " EDT :clock3:")
    elif("0330" <= timeL <= "0359"):
        await ctx.send(localtime + " EDT :clock4:")
    else:
        await ctx.send(localtime + " EDT")


@bot.command(pass_context=True)
async def fgt(ctx):
    await ctx.send("Honestly, " + (ctx.author.mention) + " I came here to have a good time and you're just making it more shite.")

@bot.command(pass_context=True)
async def fag(ctx, user: discord.Member):
    await ctx.send("Honestly, you're being such a fgt. " + (user.mention))

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
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Daddy")
async def kick(ctx, user: discord.Member):
    await ctx.send(":boot: :ear_of_rice: Not in my, {} ricefields! :ear_of_rice: :boot:".format(user.mention) )
    await discord.Member.kick(user)

@bot.event
async def on_member_join(member):

    roleq = discord.utils.get(member.guild.roles, name='&404430694408781844')
    await member.add_roles(member, roleq)

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    await ctx.send("{} gives hugs to {}!".format(ctx.author.mention, user.mention))

@bot.command(pass_context=True)
async def slap(ctx, user: discord.Member):
    import time
    localtime = time.strftime("%H%M%p")
    if( "2200PM" <= localtime <= "2359PM"):
        await ctx.send("{} tiredly slaps {}!".format(ctx.author.mention, user.mention))
    elif( "0000AM" <= localtime <= "0600AM"):
        await ctx.send("{} tiredly slaps {}!".format(ctx.author.mention, user.mention))
    else:
        await ctx.send("{} slaps {}!".format(ctx.author.mention, user.mention))



@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    guild = message.guild
    print("{}: {} {}: {}".format(guild, channel, author, content))

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    guild = message.guild
    mention = message.author.mention
    if (message.content.startswith("no u")):
        if(message.author.bot):
            print("{}: {} {}: {}".format(guild, channel, author, content))
            await bot.process_commands(message)
        else:
            print("{}: {} {}: {}".format(guild, channel, author, content))
            await message.channel.send("no u {}".format(mention))
            await bot.process_commands(message)
    elif(message.author.bot):
        print("{}: {} {}: {}".format(guild, channel, author, content))
        await bot.process_commands(message)
    else:
        print("{}: {} {}: {}".format(guild, channel, author, content))
        await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    import time
    author = message.author
    content = message.content
    channel = message.channel
    mention = message.author.mention
    avatar = message.author.avatar_url
    localtime = time.strftime("%H:%M")
    embed =discord.Embed(title="{} said:".format(author), description="{}".format(message.content), color=0x33FFD2)
    embed.add_field(name="Deleted at", value="{} EDT".format(localtime))
    embed.set_thumbnail(url=avatar)
    await message.channel.send("{}".format(mention))
    await message.channel.send(embed=embed)


#Token for discord bot goes here :P
bot.run("NDQ3NDcxOTkyNDAxMjk3NDE4.DeIH9w.2O8b11UIDMCvAX8qKutMiBtH1KQ")
