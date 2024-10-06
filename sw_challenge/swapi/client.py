import asyncio
from typing import List, Dict
import logging
import aiohttp

from ..core.utils import SWAPI_RESOURCE_TO_ENTITY_TYPE_MAP
from .models.resource import StarWarsResource
from .core.enums import ResourceEnum, ResponseParameterEnum
from .query import StarWarsAPIQuery
from ..core.person import Person
from .models.person import Person as ApiPerson
from ..core.entity import StarWarsEntity
from .core.utils import ENUM_TO_RESOURCE_MAP


class StarWarsAPIClient:

    REQUEST_TIMEOUT_MS: int = 2_000
    search_cache: Dict[str, List[StarWarsResource]] = {}
    entities_cache: Dict[str, StarWarsEntity] = {}

    async def search(self, search_term: str) -> list[StarWarsResource]:

        if search_term not in self.search_cache.keys():
            search_results = await asyncio.gather(*[self.__search_resource(resource, search_term) for resource in ResourceEnum])
            results = [i for r in search_results for i in r]
            self.search_cache[search_term] = results

        return self.search_cache[search_term]

    async def __search_resource(self, resource: ResourceEnum, term: str) -> List[StarWarsResource]:

        query = StarWarsAPIQuery().add_resource(resource).add_search_term(term).get_url()

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(query, timeout=self.REQUEST_TIMEOUT_MS) as response:

                    if not response.ok: raise Exception("Bad Request")
                    found_resources = await response.json()

            return [ENUM_TO_RESOURCE_MAP[resource](**resource_dict)
                    for resource_dict in found_resources[ResponseParameterEnum.RESULTS]]

        except Exception as e:
            logging.error(f"Failed to search for {resource} using term {term}") # TODO: why has it failed?
            raise e

    def get_by_search_term(self, search_term: str) -> list[StarWarsEntity]:

        found_resources = asyncio.run(self.search(search_term))
        previously_cached_entities = [self.entities_cache[r.url] for r in found_resources if r.url in self.entities_cache]
        new_resources = [r for r in found_resources if r.url not in self.entities_cache]
        related_people = asyncio.run(self.__get_related_people(new_resources))

        new_entities = self.__convert(found_resources, related_people)

        self.entities_cache |= {r.url: e for r, e in zip(found_resources, new_entities)}

        return new_entities + previously_cached_entities

    async def __get_related_people(self, resources: List[StarWarsResource]) -> List[Person]:

        related_people = await asyncio.gather(*[r.get_related_people() for r in resources])
        return related_people

    def __convert(self, resource_entities: List[StarWarsResource], related_people: List[List[ApiPerson]]) -> List[StarWarsEntity]:

        entities = [
            StarWarsEntity(
                e.name,
                SWAPI_RESOURCE_TO_ENTITY_TYPE_MAP[e.resource_type],
                [Person(person.name) for person in people]
            ) for e, people in zip(resource_entities, related_people)
        ]
        return entities