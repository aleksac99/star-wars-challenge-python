from typing import List

from .resource import StarWarsResource
from ...core.person import Person as CorePerson
from ..core.enums import ResourceEnum

class Person(StarWarsResource):

    resource_type: ResourceEnum = ResourceEnum.PERSON

    def __init__(self, **kwargs) -> None:

        super().__init__([kwargs['url']], **kwargs)

    async def get_related_people(self) -> List[CorePerson]:
        # NOTE: Each person is related to itself
        return [CorePerson(self.name)] # TODO: Convert to CorePerson