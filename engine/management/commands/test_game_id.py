from django.core.management.base import BaseCommand
from engine.etl import etl_games, get_account_ids, get_new_game_ids
from engine.RiotAPI import RiotAPI
from engine.constants import SUMMONER_NAMES, RIOT_API_KEY


class Command(BaseCommand):
    help = '''Runs the load process for a single game_id.'''

    def add_arguments(self, parser):
        parser.add_argument('game_id', nargs='+', type=int,
                            help='The numeric identifier of the game to be loaded.')

    def handle(self, *args, **options):
        api = RiotAPI(RIOT_API_KEY)
        account_ids = get_account_ids(SUMMONER_NAMES)
        new_games = [game for game in get_new_game_ids(api, account_ids, []) if game[0] == options['game_id'][0]]
        print(new_games)
        etl_games(api, SUMMONER_NAMES, new_games)
