from .enums import ResourceEnum
from ..models.person import Person
from ..models.vehicle import Vehicle
from ..models.starship import Starship
from ..models.species import Species
from ..models.film import Film
from ..models.planet import Planet


ENUM_TO_RESOURCE_MAP = {
    ResourceEnum.PERSON: Person,
    ResourceEnum.FILM: Film,
    ResourceEnum.STARSHIP: Starship,
    ResourceEnum.PLANET: Planet,
    ResourceEnum.VEHICLE: Vehicle,
    ResourceEnum.SPECIES: Species,
    }