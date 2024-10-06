from typing import List

from .resource import StarWarsResource
from ...core.person import Person as CorePerson
from ..core.enums import ResourceEnum

class Species(StarWarsResource):

    resource_type: ResourceEnum = ResourceEnum.SPECIES

    def __init__(self, **kwargs) -> None:

        super().__init__(kwargs['people'], **kwargs)
