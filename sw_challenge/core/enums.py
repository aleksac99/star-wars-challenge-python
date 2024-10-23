from enum import StrEnum

class Message(StrEnum):

    ENTER_SEARCH_TERM_MESSAGE = 'Please enter a Star Wars search term (q to exit): '
    EXIT_MESSAGE = 'q'

class EntityTypeEnum(StrEnum):

    PERSON = 'Person'
    VEHICLE = 'Vehicle'
    STARSHIP = 'Starship'
    PLANET = 'Planet'
    FILM = 'Film'
    SPECIES = 'Species'