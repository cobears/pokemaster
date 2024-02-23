from pokemaster.utils.api import PokeBaseApi


class Pokemon:
    def __init__(self, name: str):
        """
        :name: str to extract pokemon information from api
        """
        pokemon = PokeBaseApi.get_pokemon(name)

        self.name = pokemon.name
        self.id = int(pokemon.id_)
        self.types = [str(x.type) for x in pokemon.types]
