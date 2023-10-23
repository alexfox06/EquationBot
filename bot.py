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

def pow(a, b):
    return a**b #this is the exponants, so it would be a to the power of b


#basic opporations
@bot.command()
async def calculate(ctx, num1, operation, num2, num3, num4):
    #I can add more numbers if needed but this is what I have so far 
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
def calculate_expression(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for token in expression.split():
        if token.isnumeric():
            output.append(token)
        elif token in operators:
            while (stack and stack[-1] in operators and
                    operators[token] <= operators[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the left parenthesis
    
    while stack:
        output.append(stack.pop())

    result_stack = []
    for token in output:
        if token.isnumeric():
            result_stack.append(token)
        elif token in operators:
            a = result_stack.pop()
            b = result_stack.pop()
            c = result_stack.pop()
            d = result_stack.pop()



            if token == '+':
                result_stack.append(str(int(a) + int(b) + int(c) + int(d)))
            elif token == '-':
                result_stack.append(str(int(a) - int(b) - int(c) - int(d)))
            elif token == '*':
                result_stack.append(str(int(a) * int(b) * int(c) * int(d)))
            elif token == '/':
                result_stack.append(str(int(a) / int(b) / int(c) / int(d)))
            elif token == '^':
                result_stack.append(str(int(a) ** int(b)))
    
    return result_stack[0]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def calculate(ctx, *, expression):
    try:
        result = calculate_expression(expression)
        await ctx.send(f'Result: {result}')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

bot.run('TOKEN')
    #if operation == "()":
        #output = #add/subtract/divide/multiply whatevers in the parenthesis 
    #elif operation == "**":
       # output = #this goes second so (exponants) 
    #elif operation == "*":
        #output = #this goes third along with division
    #elif operation == "/":
        #output = #this goes at the same time as multipication (not higher, not lower, unless its first in the operation ie. 2 / 9 * 3)
    #elif operation == "-":
        #output = #this goes after everything at the same time as addition
    #elif operation = "+":
        #output = #same time as subtraction 
        






bot.run(TOKEN)
