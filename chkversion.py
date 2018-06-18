import discord
from discord import opus
from discord.ext import commands
from discord.ext.commands import bot
import os

print("SSNBot version checker booting")

if(discord.__version__ == "0.16.12"):
    exec(open("reSSNBot.py").read())
else:
    print("SSNBot Does not have the right version of Discord.py, I'm running version {}".format(discord.__version__))


# os.listdir()
