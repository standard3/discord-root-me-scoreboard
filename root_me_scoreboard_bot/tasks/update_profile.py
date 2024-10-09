from loguru import logger

from discord.ext.commands import Bot, Cog

class UpdateProfile(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
