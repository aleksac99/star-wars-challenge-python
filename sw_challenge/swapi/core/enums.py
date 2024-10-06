from enum import StrEnum

class ResourceEnum(StrEnum):

    PERSON = 'people'
    VEHICLE = 'vehicles'
    STARSHIP = 'starships'
    PLANET = 'planets'
    FILM = 'films'
    SPECIES = 'species'

class ResponseParameterEnum(StrEnum):

    RESULTS = 'results'