import os
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
        img_url = get(sticker_id, index)
        if img_url:
            await ctx.respond(img_url)
        else:
            await ctx.respond("Failed!")

    bot.run(TOKEN)
