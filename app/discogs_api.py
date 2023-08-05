import discogs_client

import configparser


class DiscogsAPI:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self._user_name = config.get('Discogs', 'user_name'), 
        self._user_token = config.get('Discogs', 'user_token')
        self.client = discogs_client.Client(user_agent=user_name, user_token=user_token)


discogs_api = DiscogsAPI()


