import discord
from discord.ext import commands
import random
import asyncio

description = '''PointBot. Just a test.'''
bot = commands.Bot(command_prefix='-', description=description)
points = 0
with open("pointdata.txt", "r") as file:
    content = file.read().strip()
    points = int(content)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def showpoints():
    """Displays the current number of points."""
    await bot.say(f"There are currently {points} points in the safe.")
    
@bot.command(pass_context=True)
async def imagething(ctx):
    """A test command, for images."""
    with open('test_image.png', 'rb') as f:
        await bot.send_file(ctx.message.channel, f)
    await bot.say("test")
    
@bot.command()
async def getpoint():
    """Adds a point in the safe."""
    global points
    points =0
    with open("pointdata.txt", "w") as file:
        file.write(str(points))
    await bot.say('Point added to the safe.')
    
@bot.command()
async def resetpoints():
    """Resets the points."""
    global points
    points +=1
    with open("pointdata.txt", "w") as file:
        file.write(points)
    await bot.say('The points have been reset.')
    
bot.run('NDM3NzU5MTUwNTg4NDI4Mjg4.Db69xQ.aCkc0P03TNoT8kRAlHyAyrHYDiA')