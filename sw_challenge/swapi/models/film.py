from typing import List

from .resource import StarWarsResource
from ...core.person import Person
from ..core.enums import ResourceEnum

class Film(StarWarsResource):

    resource_type: ResourceEnum = ResourceEnum.FILM

    def __init__(self, **kwargs) -> None:

        super().__init__(
            kwargs['characters'],
            **kwargs)

        self.other_people =  kwargs['director'].split(', ') + kwargs['producer'].split(', ')