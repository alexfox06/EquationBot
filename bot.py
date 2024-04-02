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
















#all the math stuff for the calculator (PEMDAS included)




def add(a, b, c, d):
   return a + b + c + d




def subtract(a, b, c, d):
   return a - b - c - d




def multiply(a, b, c, d):
   return a * b * c * d




def divide(a, b, c, d):
   return a / b / c / d


def pow(a, b):
   return a**b #this is the exponants, so it would be a to the power of b (second number in this expression will always be defined as b)




#basic opporations
@bot.command()
async def calculate(ctx, num1, operation, num2, num3, num4):
   #I can add more numbers if needed but this is what I have so far
   a = int(num1) 
   b = int (num2)
   c = int (num3)
   d = int (num4)




@bot.command()
async def add(ctx, num1: float, num2: float):
   try:
       result = num1 + num2
       await ctx.send(f'{num1} + {num2} = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')




   if operation == "+":
       output = add(a, b, c, d)




       @bot.command()
async def subtract(ctx, num1: float, num2: float):
   try:
       result = num1 - num2
       await ctx.send(f'{num1} - {num2} = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')




   elif operation == "-":
       output = subtract(a, b, c, d)




        @bot.command()
async def multiply(ctx, num1: float, num2: float):
   try:
       result = num1 * num2
       await ctx.send(f'{num1} * {num2} = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')




   elif operation == "*":
       output = multiply(a, b, c, d)




       @bot.command()
async def divide(ctx, num1: float, num2: float):
   try:
       result = num1 / num2
       await ctx.send(f'{num1} / {num2} = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')




   elif operation == "/":
       output = divide(a, b, c, d)
       #error message for if user inputs something wrong




   else:
       output = "plese input another opperation; the one inputted has an error"
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
           stack.pop() 
  
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
   if operation == "()":
       output = add(a, b, c, d), subtract(a,b,c,d), multiply(a,b,c,d), divide(a,b,c,d)
   elif operation == "**":
       output = multiply(a**b)
   elif operation == "*":
       output = multiply(a,b,c,d)
   elif operation == "/":
       output = divide(a,b,c,d)
   elif operation == "-":
       output = subtract(a,b,c,d)
   elif operation = "+":
       output = add(a,b,c,d)


       #derivative trouble shootong code I will move it later but I also have no idea how derivative works
       @bot.command()
async def calculate(ctx, *, expression):
   try:
       result = sp.sympify(expression)
       await ctx.send(f'Result: {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')


@bot.command()
async def derivative(ctx, *, expression):
   try:
       derivative = calculate_derivative(expression)
       await ctx.send(f'Derivative: {derivative}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')


       #sin code
       @bot.command()
async def sin(ctx, value: float):
   try:
       result = math.sin(math.radians(value))
       await ctx.send(f'sin({value}) = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')


       #cos code
       @bot.command()
async def cos(ctx, value: float):
   try:
       result = math.cos(math.radians(value))
       await ctx.send(f'cos({value}) = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')


       #tan code
       @bot.command()
async def tan(ctx, value: float):
   try:
       result = math.tan(math.radians(value))
       await ctx.send(f'tan({value}) = {result}')
   except Exception as e:
       await ctx.send(f'Error: {str(e)}')
      










      


      


      






bot.run(TOKEN)


