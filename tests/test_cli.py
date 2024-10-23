from sw_challenge.swapi.client import StarWarsAPIClient
from sw_challenge.cli import CLI

def test_cli(monkeypatch, capsys):

    inputs = iter(['tatoo', 'x-wing', 'LEI', 'q'])

    expected_outputs = [
        "Tatooine | Planet | Luke Skywalker, C-3PO, Darth Vader, Owen Lars, Beru Whitesun lars, R5-D4, Biggs Darklighter, Anakin Skywalker, Shmi Skywalker, Cliegg Lars",
        "X-wing | Starship | Luke Skywalker, Biggs Darklighter, Wedge Antilles, Jek Tono Porkins",
        "Leia Organa | Person | Leia Organa"
    ]

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    cli = CLI()
    cli.run()

    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')

    assert outputs == expected_outputs