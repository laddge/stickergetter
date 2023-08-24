import os
from io import BytesIO
from dotenv import load_dotenv
import discord
from discord import Option
from .get import get


def main():
    env_path = os.path.join(os.path.dirname(__file__), "../.env")
    load_dotenv(env_path)

    TOKEN = os.getenv("DISCORD_TOKEN")

    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"ready as {bot.user}")

    @bot.slash_command(description="Return LINE sticker's image url")
    async def sticker(
        ctx: discord.ApplicationContext,
        sticker_id: Option(int, required=True),
        index: Option(int, required=True),
    ):
        img = get(sticker_id, index)
        if img:
            buff = BytesIO(img)
            buff.seek(0)
            await ctx.respond(file=discord.File(fp=buff, filename="sticker.png"))
        else:
            await ctx.respond("Failed!")

    bot.run(TOKEN)
