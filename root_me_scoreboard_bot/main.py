from loguru import logger

from discord import Intents
from discord.ext.commands import Bot

from root_me_scoreboard_bot import commands, tasks
from root_me_scoreboard_bot.utils.config import DISCORD_TOKEN

# Setup discord intents
intents = Intents.default()
intents.message_content = True
intents.members = True

# Create Bot
bot: Bot = Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready() -> None:
    """Logs when the Bot is ready to run"""

    logger.info(f"Logged in as {bot.user}")

    # Import all commands handlers
    logger.info(f"Importing all commands handlers")
    await commands.setup(bot)

    # Import all tasks handlers
    logger.info(f"Importing all tasks handlers")
    await tasks.setup(bot)

    logger.info(f"Ready to run")


bot.run(DISCORD_TOKEN)
