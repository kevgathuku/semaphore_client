from hammock import Hammock as SemaphoreClient

from .secret import Secret
from .team import Team
from .user import User

API_URL = "https://api.semaphoreci.com"
API_VERSION = "v2"
BASE_URL = f'{API_URL}/{API_VERSION}/'


class Semaphore(object):

    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.client = SemaphoreClient(BASE_URL,
                                headers={'Authorization': f'Token {self.auth_token}'})

    def teams(self):
        return Team(self.client)

    def secrets(self):
        return Secret(self.client)

    def users(self):
        return User(self.client)
