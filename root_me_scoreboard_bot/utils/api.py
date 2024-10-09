import aiohttp
import json
from dataclasses import dataclass
from enum import Enum

from loguru import logger
from pydantic import BaseModel, Field

from root_me_scoreboard_bot.utils.config import ROOTME_API_TOKEN


class User(BaseModel):
    """Root-me API User object"""

    name: str = Field(alias="nom")
    id: int = Field(alias="id_auteur")
    status: str | None = Field(alias="statut")
    logo_url: str | None
    score: int | None
    position: int | None
    is_premium: bool | None = Field(alias="membre")
    challenges: list[str] | None
    solutions: list[str] | None
    validations: list[str] | None


class Categories(Enum):
    """Maps category IDs to their string counterpart"""

    APP_SCRIPT = "189"
    APP_SYSTEME = "203"
    CRACKING = "69"
    CRYPTANALYSE = "18"
    FORENSIC = "208"
    PROGRAMMATION = "17"
    REALISTE = "70"
    RESEAU = "182"
    STEGANOGRAPHIE = "67"
    WEB_CLIENT = "16"
    WEB_SERVEUR = "68"

    @classmethod
    def get_category(cls, id_value):
        return CATEGORIES.get(id_value, "Unknown")


@dataclass
class Endpoints:
    """Root-me endpoints"""

    endpoint: str = "https://api.www.root-me.org"
    authors: str = f"{endpoint}/auteurs"
    challenges: str = f"{endpoint}/challenges"


class API:
    """to-do"""

    # FIXME: bad return type
    async def get(self, endpoint: str) -> None:
        """to-do"""

        headers = {"User-Agent": ""}
        cookies = {"api_key": ROOTME_API_TOKEN}

        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.get(endpoint) as response:
                if response.status != 200:
                    logger.debug(
                        f"Request to endpoint '{endpoint}' failed with status {response.status}"
                    )
                    return None
                resp = await response.json()

        return resp

    # FIXME: bad return type
    async def get_user_by_id(self, _id: int) -> User | None:
        """to-do"""
        endpoint = f"{Endpoints.authors}/{str(_id)}"

        response = await self.get(endpoint)
        if not response:
            return None

        return User(**response)

    # FIXME: bad return type
    async def get_all_users_by_name(self, name: str) -> list[str] | None:
        """to-do"""
        endpoint = f"{Endpoints.authors}?nom={name}"

        return self.get(endpoint)

    # FIXME: bad return type
    async def get_challenge_by_id(self, _id: int) -> str | None:
        """to-do"""
        endpoint = f"{Endpoints.challenges}/{str(_id)}"

        return self.get(endpoint)

    # FIXME: bad return type
    async def get_challenges_by_name(self, name: str) -> list[str] | None:
        """to-do"""
        endpoint = f"{Endpoints.challenges}?titre={name}"

        return self.get(endpoint)
