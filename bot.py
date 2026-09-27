import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


DAILY_REWARD = 150

wallets = {}

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


for item in MODELS:
    text += f"{counter}. {item['model']}, Value: {item['value']}\n"
    counter += 1


def get_balance(user_id):
    if user_id not in wallets:
        wallets[user_id] = 0

    return wallets[user_id]


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
async def wallet(ctx):
    user_id = str(ctx.author.id)
    balance = get_balance(user_id)

    await ctx.send(f"{ctx.author.mention}, your wallet balance is: {balance} coins.")


@bot.command()
async def daily(ctx):
    user_id = str(ctx.author.id)
    new_balance = get_balance(user_id) + DAILY_REWARD
    wallets[user_id] = new_balance

    await ctx.send(
        f"{ctx.author.mention}, you received {DAILY_REWARD} coins! "
        f"Your new balance is: {new_balance} coins."
    )


@bot.command()
async def model(ctx, numero: int):
    if 1 <= numero <= len(MODELS):
        chosen = MODELS[numero - 1]
        await ctx.send(f"Model {numero} selected: {chosen['model']}, Value: {chosen['value']}")
    else:
        await ctx.send("Invalid model number!")


@bot.command()
async def models(ctx):
    await ctx.send(f"Available models:\n{text}")


bot.run(TOKEN)