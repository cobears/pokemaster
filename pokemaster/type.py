from pokemaster.utils.api import PokeBaseApi

class Type:
    def __init__(self, name: str) -> None:
        """_summary_

        Args:
            name (str): _description_
        """
        type = PokeBaseApi.get_type(name)

        self.id = type.id_
        self.name = type.name
        self.damage_relations = {key: list(map(str, item)) for key, item in vars(type.damage_relations).items()}

        # single damage multiplier is not within the self.damage_relations, so lets add it
        self.damage_relations.update({
            "single_damage_to": [],
            "single_damage_from": [],
        })
        
        all_types = PokeBaseApi.get_all_types()
        for t in all_types:
            if t in self.damage_relations.values(): continue
            else:
                self.damage_relations['single_damage_to'].append(t)
                self.damage_relations['single_damage_from'].append(t)