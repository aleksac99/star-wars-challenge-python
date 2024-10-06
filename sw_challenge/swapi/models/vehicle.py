from typing import List

from .resource import StarWarsResource
from ...core.person import Person as CorePerson
from ..core.enums import ResourceEnum

class Vehicle(StarWarsResource):

    resource_type: ResourceEnum = ResourceEnum.VEHICLE

    def __init__(self, **kwargs) -> None:

        super().__init__(kwargs['pilots'], **kwargs)
