import pokebase as pb
from typing import Optional


class PokeBaseApi:
    def __init__(self, **kwargs):
        self.api_fn = pb.APIResource
        self.api_ls = pb.APIResourceList
        self.api_meta = pb.APIMetadata
        self.sprite_fn = pb.SpriteResource

    @staticmethod
    def get_pokemon(name: str, pokedex_id: Optional[int] = None) -> pb.APIResource:
        """get_pokemon takes a name and retrieves information form the PokeAPI

        Args:
            name (str): pokemon name
            pokedex_id (Optional[int]): pokedex reference number

        Returns:
            pb.APIResource: PokeAPI object class for the given pokemon
        """
        return pb.pokemon(name.lower())

    @staticmethod
    def get_type(name: str) -> pb.APIResource:
        """_summary_

        Args:
            name (str): _description_

        Returns:
            pb.APIResource: _description_
        """
        return pb.type_(name)

    @staticmethod
    def get_all_types():
        return [str(pokemon_type) for pokemon_type in pb.type_("all").results]
