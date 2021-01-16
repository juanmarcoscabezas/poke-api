from django.core.management.base import BaseCommand, CommandError
import requests
from pokemon.models import Pokemon

class Command(BaseCommand):
    help = 'Adds the specific Evolution Chain.'

    def add_arguments(self, parser):
        parser.add_argument('evolution_chain_ids', nargs="+", type=int)
    
    def handle(self, *args, **options):
        for evolution_chain_id in options['evolution_chain_ids']:
            is_evolution_chain_made = get_evolution_chain(self, evolution_chain_id)
            if is_evolution_chain_made is None:
                self.stdout.write(self.style.ERROR('Evolution Chain {} does not exist'.format(evolution_chain_id)))
            else:
                self.stdout.write(self.style.SUCCESS('Succesfully added Evolution chain "%s"' %evolution_chain_id))
            break

def get_evolution_chain(self, evolution_chain_id):
    url = 'https://pokeapi.co/api/v2/evolution-chain/{}'.format(evolution_chain_id)
    response = requests.get(url=url)
    if (response.status_code == 404):
        return None
    evolution_chain = response.json()
    chain = evolution_chain['chain']
    evolves_to = [chain]
    get_all_evolutions(evolves_to, None)
    return True
    
def get_all_evolutions(evolves_to, evolves_from):
    for evolution in evolves_to:
        pokemon_id = get_pokemon_id(evolution['species']['url'])
        get_pokemon_from_api(pokemon_id, evolves_from)
        if len(evolves_to) > 1:
            get_all_evolutions(evolution['evolves_to'], evolves_from)
        else:
            get_all_evolutions(evolution['evolves_to'], pokemon_id)
    return None

def get_pokemon_id(url):
    pokemon_id = url.split('/')[-2]
    return pokemon_id

def get_pokemon_from_api(id, evolves_from):
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(id)
    response = requests.get(url=url)
    if (response.status_code == 404):
        self.stdout.write(self.style.ERROR('Pokemon {} does not exist'.format(id)))
        return None
    pokemon = response.json()
    new_pokemon = {
        'id': pokemon['id'],
        'name': pokemon['name'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'image': pokemon['sprites']['front_default'] if pokemon['sprites']['front_default'] is not None else pokemon['sprites']['back_default']
    }
    if evolves_from is not None:
        pokemon_parent = Pokemon.objects.get(id=evolves_from)
        new_pokemon['evolves_from'] = pokemon_parent
    for stat in pokemon['stats']:
        stat_name = stat['stat']['name'].replace('-', '_')
        new_pokemon[stat_name] = stat['base_stat']
    Pokemon(**new_pokemon).save()