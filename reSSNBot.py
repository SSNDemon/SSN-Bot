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

@bot.command
async def ping(ctx):
    bot.send(":ping_pong: Pong!")


bot.run("NDQ3NDcxOTkyNDAxMjk3NDE4.DeIH9w.2O8b11UIDMCvAX8qKutMiBtH1KQ")
