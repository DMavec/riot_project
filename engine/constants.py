RIOT_API_KEY = open('engine/credentials/riot_key.txt').read()

URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{static}{url}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'game': 'v{version}/game/by-summoner/{id}/recent',
    'lol-static-data': 'v{version}/{end_url}',
    'match-recent': 'match/v{version}/matchlists/by-account/{id}?beginIndex={begin_index}',
    'match': 'match/v{version}/matches/{id}'
}

API_VERSIONS = {
    'summoner': '3',
    'game': '1.3',
    'match': '3',
    'lol-static-data': '3'
}

REGIONS = {
    'oceania': 'oc1'
}

SUMMONER_NAMES = [
    'diggs',
    'bumster',
    'mwaxy',
    'loui8sdstk',
    'smatties',
    'skandaras',
    'menelaus34',
    'dicedstk',
    'loui9sdstk',

    # 'endgamedos',
    # '2dmin'
    # 'pangryanda',
    # 'ridethellama',
    # 'orangu',
    # 'shaarcer',
    # 'sellerie',
    # 'muncheroo',
    # 'splunkle',
    # 'minisundae',
    # 'themrb',
    # 'panman',
    # 'saltimate',
    # 'thereisnosaurus',
    # 'kkfizzban'
]
