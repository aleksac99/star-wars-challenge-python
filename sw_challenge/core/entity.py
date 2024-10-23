from typing import List

from .person import Person
from .enums import EntityTypeEnum

class StarWarsEntity:

    def __init__(self, name: str, entity_type: EntityTypeEnum, related_people: List[Person]) -> None:

        self.name = name
        self.entity_type = entity_type
        self.related_people = related_people

    def __str__(self) -> str:
        return f'{self.name} | {self.entity_type} | ' + ', '.join([str(p) for p in self.related_people])
    
    def __repr__(self) -> str:
        return str(self)