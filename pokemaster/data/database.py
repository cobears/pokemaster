from pokemaster.utils.api import PokeBaseApi

class Pokemon:
    def __init__(self, name: str):
        """
        :name: str to extract pokemon information from api
        """
        pokemon = PokeBaseApi.get_pokemon(name)

        self.name = pokemon.name
        self.pokedex = int(pokemon.id_)
        self.type = [str(x.type) for x in pokemon.types]


class Type:
    def __init__(self, name: str) -> None:
        """_summary_

        Args:
            name (str): _description_
        """
        type = PokeBaseApi.get_type(name)

        self.id = type.id_
        self.name = type.name
        self.damage_relations = {key:item for key, item in vars(type.damage_relations).items()}