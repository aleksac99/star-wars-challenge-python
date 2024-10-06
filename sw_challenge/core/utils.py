from .enums import EntityTypeEnum
from ..swapi.core.enums import ResourceEnum

ENTITY_TYPE_TO_SWAPI_RESOURCE_MAP = {
    EntityTypeEnum.PERSON: ResourceEnum.PERSON,
    EntityTypeEnum.VEHICLE: ResourceEnum.VEHICLE,
    EntityTypeEnum.STARSHIP: ResourceEnum.STARSHIP,
    EntityTypeEnum.PLANET: ResourceEnum.PLANET,
    EntityTypeEnum.FILM: ResourceEnum.FILM,
    EntityTypeEnum.SPECIES: ResourceEnum.SPECIES,
    }
SWAPI_RESOURCE_TO_ENTITY_TYPE_MAP = {v: k for k, v in ENTITY_TYPE_TO_SWAPI_RESOURCE_MAP.items()}