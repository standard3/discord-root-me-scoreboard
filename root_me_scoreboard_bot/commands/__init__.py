from loguru import logger

from discord.ext.commands import Bot

# from .update_profile import UpdateProfile


async def setup(bot: Bot) -> None:
    """
    Add all Cogs (commands) to the bot
    :param bot: Discord Bot where commands are registered.
    """
    # await bot.add_cog(UpdateProfile(bot))

    logger.info(f"All commands handlers successfully loaded")
