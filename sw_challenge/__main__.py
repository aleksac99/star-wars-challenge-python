from .core.enums import Message
from .swapi.client import StarWarsAPIClient

def main():

    client = StarWarsAPIClient()

    while True:

        search_term = input(Message.ENTER_SEARCH_TERM_MESSAGE + ': ')
        if search_term.lower() == Message.EXIT_MESSAGE: break
        found_entities = client.get_by_search_term(search_term)
        for entity in found_entities:
            print(entity)

if __name__ == '__main__':
    main()