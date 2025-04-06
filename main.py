import discord
from discord.ext import commands
import os
import asyncio

print("⚙️ main.py wordt gestart...")

TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = 1356894863454376105

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is ingelogd als {bot.user}")
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ Slash commands gesynchroniseerd met GUILD {guild.id} ({len(synced)} commando's)")
    except Exception as e:
        print(f"❌ Slash sync error: {e}")
    await load_cogs()

async def load_cogs():
    try:
        await bot.load_extension("commands.ping")
        print("✅ ping.py geladen")
    except Exception as e:
        print(f"❌ Fout bij laden ping.py: {e}")

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())