import backoff
import requests
from time import sleep
from engine.constants import REGIONS, URL, API_VERSIONS, SUMMONER_NAMES

class RiotAPI(object):
    def __init__(self, api_key, region=REGIONS['oceania']):
        self.api_key = api_key
        self.region = region

    @backoff.on_exception(backoff.expo,
                          requests.RequestException,
                          max_value=32)
    def _request(self, api_url, static=False, params={}):
        # Put additional parameters into args
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value

        # print(URL['base'].format(
        #     proxy=self.region,
        #     static='static-data/' if static else '',
        #     region=self.region,
        #     url=api_url
        # ))

        retries = 1
        while 0 < retries < 5:
            response = requests.get(
                URL['base'].format(
                    proxy=self.region,
                    static='static-data/' if static else '',
                    region=self.region,
                    url=api_url
                ),
                params=args
            )

            if 'status' in response.json().keys():
                retries += 1
                sleep(30)
            else:
                retries = 0

        return response.json()

    def get_summoner_by_name(self, name):
        api_url = URL['summoner_by_name'].format(
            version=API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)

    def get_recent_matches(self, id, begin_index=0):
        api_url = URL['match-recent'].format(
            version=API_VERSIONS['match'],
            id=id,
            begin_index=begin_index
        )
        return self._request(api_url)

    def get_match(self, id):
        api_url = URL['match'].format(
            version=API_VERSIONS['match'],
            id=id
        )
        return self._request(api_url)

    def update_static_summoner_ids(self):
        ids = {}
        for name in SUMMONER_NAMES:
            print('Retrieving =>' + name)
            try:
                id = self.get_summoner_by_name(name)[name]['id']
                ids[id] = name
            except:
                print('WARNING: Name not found.')

        target = open('static_summoner_ids.txt', 'w')
        target.write(str(ids))

    # lol-static-data-v3
    def _static_request(self, end_url):
        return self._request(
            URL['lol-static-data'].format(
                version=API_VERSIONS['lol-static-data'],
                end_url=end_url
            ),
            static=True
        )

    def static_get_champion(self, champ_id):
        return self._static_request(
            'champions/{id}'.format(id=champ_id),
        )
