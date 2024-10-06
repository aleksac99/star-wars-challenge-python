from .core.enums import ResourceEnum

class StarWarsAPIQuery:

    BASE_URL: str = 'https://swapi.dev/api'
    SEARCH_PARAM: str = 'search'

    def __init__(self) -> None:

        self.url = self.BASE_URL

    def add_search_term(self, term: str) -> "StarWarsAPIQuery":

        self.url += f'/?{self.SEARCH_PARAM}={term}'
        return self

    def get_url(self) -> str:

        return self.url

    def add_resource(self, resource: ResourceEnum) -> "StarWarsAPIQuery":

        self.url += f'/{resource}'

        return self