import time
import aiohttp
import asyncio
from typing import List
from abc import ABC

from ..core.enums import ResourceEnum
from ...core.person import Person

class StarWarsResource(ABC):

    resource_type: ResourceEnum

    def __init__(self, related_people_url: List[str], **kwargs) -> None:

        self.name = kwargs.get('name', kwargs.get('title'))
        self.url = kwargs['url']
        self.__related_people = related_people_url

    async def get_related_people(self) -> List[Person]:

        async with aiohttp.ClientSession() as session:

            requests = [self.__fetch(session, query) for query in self.__related_people]
            responses = await asyncio.gather(*requests)

        return [Person(r['name']) for r in responses]

    async def __fetch(self, session: aiohttp.ClientSession, query: str):

        async with session.get(query) as response:
            return await response.json()
        
    def __str__(self):
        return f'{self.name} ({self.resource_type})'