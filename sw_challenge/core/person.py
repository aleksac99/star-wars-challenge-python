# from .entity import StarWarsEntity


class Person:

    def __init__(self, name: str) -> None:

        self.name = name

    def __str__(self) -> str:
        return self.name
        
    def __repr__(self) -> str:
        return str(self)