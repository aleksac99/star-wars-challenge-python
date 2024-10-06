from typing import List

from .resource import StarWarsResource
from ...core.person import Person as CorePerson
from ..core.enums import ResourceEnum

class Starship(StarWarsResource):

    resource_type: ResourceEnum = ResourceEnum.STARSHIP

    def __init__(self, **kwargs) -> None:

        super().__init__(kwargs['pilots'], **kwargs)
