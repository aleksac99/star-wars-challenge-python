import asyncio

from sw_challenge.swapi.client import StarWarsAPIClient
from sw_challenge.swapi.query import StarWarsAPIQuery


def test_query():

    query = StarWarsAPIQuery().add_resource("people").add_search_term('ale').get_url()
    assert query == "https://swapi.dev/api/people/?search=ale"

def test_client():

    client = StarWarsAPIClient()

    # Test search
    results = asyncio.run(client.search('tatoo'))
    results_str = '\n'.join([str(r) for r in results])

    assert results_str == 'Tatooine (planets)'

    # Test related people
    results = client.get_by_search_term('revenge')
    results_str = '\n'.join([str(r) for r in results])
    assert results_str == 'Revenge of the Sith | Film | Luke Skywalker, C-3PO, R2-D2, Darth Vader, Leia Organa, Owen Lars, Beru Whitesun lars, Obi-Wan Kenobi, Anakin Skywalker, Wilhuff Tarkin, Chewbacca, Yoda, Palpatine, Nute Gunray, Padmé Amidala, Ayla Secura, Mace Windu, Ki-Adi-Mundi, Kit Fisto, Eeth Koth, Adi Gallia, Saesee Tiin, Plo Koon, Poggle the Lesser, Luminara Unduli, Dooku, Bail Prestor Organa, R4-P17, Shaak Ti, Grievous, Tarfful, Raymus Antilles, Sly Moore, Tion Medon'