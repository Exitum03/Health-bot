# libs
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="-")
token = ""


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")


@bot.command()
async def wisdom(ctx, *, question):
    response = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(f"Question: {question} "
                   f"\n Answer: {random.choice(response)}")

bot.run(token)