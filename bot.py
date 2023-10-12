#imports
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os


#loading in the token
load_dotenv()


TOKEN = os.getenv("TOKEN")


#coding our bot
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=".", intents=intents)








#all the math stuff


def add(a, b, c, d):
    return a + b + c + d


def subtract(a, b, c, d):
    return a - b - c - d


def multiply(a, b, c, d):
    return a * b * c * d


def divide(a, b, c, d):
    return a / b / c / d


#basic opporations
@bot.command()
async def calculate(ctx, num1, operation, num2, num3, num4):
    a = int(num1)  
    b = int (num2)
    c = int (num3)
    d = int (num4)



    if operation == "+":
        output = add(a, b, c, d)
    elif operation == "-":
        output = subtract(a, b, c, d)
    elif operation == "*":
        output = multiply(a, b, c, d)
    elif operation == "/":
        output = divide(a, b, c, d)
    else:
        output = "nope"
    await ctx.send(output)









bot.run(TOKEN)
