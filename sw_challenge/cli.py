from .core.enums import Message
from .swapi.client import StarWarsAPIClient


class CLI:

    def __init__(self):
        pass

    def run(self):

        client = StarWarsAPIClient()

        while True:

            search_term = input(Message.ENTER_SEARCH_TERM_MESSAGE + ': ')
            if search_term.lower() == Message.EXIT_MESSAGE: break
            found_entities = client.get_by_search_term(search_term)
            for entity in found_entities:
                print(entity)