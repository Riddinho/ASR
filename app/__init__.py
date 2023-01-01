import configparser
from . import discogs_api as api

def create_config(config_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

class App:
    def __init__(self, config):
        self.config = config
        self.discogs_client = api.DiscogsAPI(
           (
               config.get("Discogs", "user_name"),
               config.get("Discogs", "user_token"),
           )
        )
        self.data = self.discogs_client.fetch()

