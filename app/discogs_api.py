import discogs_client



class DiscogsAPI:
    def __init__(self, auth):
        self.client = discogs_client.Client(user_agent=auth[0], user_token=auth[1])

    def fetch(self):
        return [True, False, True]





