import pokebase as pb

class DataBase:
    def __init__(self, **kwargs):
        self.api_fn = pb.APIResource
        self.api_ls = pb.APIResourceList
        self.api_meta = pb.APIMetadata
        self.sprite_fn = pb.SpriteResource
    
    def find_pokemon(self, name: str) -> pb.APIResource:
        return pb.pokemon(name)