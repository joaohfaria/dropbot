import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

MODELOS = ["AK-47", "M4A1", "AWP", "Pistolas", "Facas", "Luvas"]

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} está online!")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def salve(ctx):
    await ctx.send(f"Salve, {ctx.author.mention}!")


@bot.command()
async def modelo(ctx, numero):
    try:
        escolha = int(numero)

        if 1 <= escolha <= len(MODELOS):
            await ctx.send(f"Modelo {escolha} selecionado: {MODELOS[escolha - 1]}")
        else:
            await ctx.send("Número de modelo inválido!")

    except ValueError:
        await ctx.send("Por favor, insira um número válido!")

texto = ""
contador = 1


for modelo in MODELOS:
    texto += f"{contador}. {modelo}\n"
    contador += 1


@bot.command()
async def modelos(ctx):
    await ctx.send(f"Modelos disponíveis:\n{texto}")

bot.run(TOKEN)