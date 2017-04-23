# importing
try:
    import asyncio
    import discord
    from discord.ext import commands
    import random
    import manipulation
except Exception:
    print('Error: Could not import modules')

# Configuration Table:
# You configure your bot in here.
configuration = [
'prefix': 'y!',
'creator': 'You',
'version': '0.1',
'description': 'Your Bot'
]

bot = commands.Bot(command_prefix=configuration['prefix'], description=configuration['description'])
# Now, let's learn creating commands:
# In Python 3.4 or 3.5 as well as 3.6, a command uses @asyncio.coroutine and @bot.command() as decorators
# A decorator marks the purpose of a function
# For example, @asyncio.coroutine marks a coroutine

@bot.event
@asyncio.coroutine
def on_ready():
    # On ready, the bot will do what you say. For example:
    print('Hello')

@bot.command()
@asyncio.coroutine
def myCommand():
    # @bot.command() and @asyncio.coroutine are required for every command.
    # You can use bot.say to talk.
    # However, you must use 'yield from' to signal a coroutine
    yield from bot.say('I just used discord.py for a command! I am a wiz!')
    # What this will do is up to you.

@bot.command(pass_context=True)
@asyncio.coroutine
# When using pass_context you are passing parts to the bot.
def question(ctx, quest : str):
    yield from bot.say('I will not answer {0}'.format(quest))
    # Formats the string

@bot.command(pass_context=True)
@asyncio.coroutine
def isNumber(ctx, number : str):
    # This will check if number is a number
    # We will use the manipulation module
    checking = manipulation.isInteger(number)
    if checking == True:
        yield from bot.say('Yes')
    elif checking == False:
        yield from bot.say('No')

# So, we learned:
# How to ask a question
# How to make a bot talk
# How to use other modules in your bot
# You can also use your info for a help command. configuration['creator']
# Thank you for using! I can't wait to see what you make!

bot.run('token')
# Replace token with your bot's token
