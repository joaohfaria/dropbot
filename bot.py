import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


MODELS = [
    {"model": "AK-47", "value": 270},
    {"model": "M4A1", "value": 310},
    {"model": "AWP", "value": 475},
    {"model": "Pistol", "value": 300},
    {"model": "Knife", "value": 300},
    {"model": "Gloves", "value": 100}
]


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)


text = ""
counter = 1


for modelo in MODELS:
    text += f"{counter}. {modelo['model']}, Value: {modelo['value']}\n"
    counter += 1


@bot.event
async def on_ready():
    print(f"{bot.user} It's online!")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def salve(ctx):
    await ctx.send(f"Hey there, {ctx.author.mention}!")


@bot.command()
async def model(ctx, numero):
    try:
        choice = int(numero)

        if 1 <= choice <= len(MODELS):
            await ctx.send(f"Model {choice} selected: {MODELS[choice - 1]['model']}, Value: {MODELS[choice - 1]['value']}")
        else:
            await ctx.send("Invalid model number!")

    except ValueError:
        await ctx.send("Please insert a valid number!")


@bot.command()
async def models(ctx):
    await ctx.send(f"Available models:\n{text}")




bot.run(TOKEN)