# %%
import time
import hashlib
import requests
from requests.auth import HTTPBasicAuth
import os

env = os.environ

class WebpageMonitor:
    """
    TODO:
    """
    def __init__(self, url='http://users.encs.concordia.ca/~cc/soen6441/', verbose=False) -> None:
        self.url = url
        self.frequency = 60
        self.last_hash = None
        self.verbose = verbose

    def __log(self, message):
        if self.verbose:
            print(f'LOG: {message}')

    def get_hash(self):
        """
        Gets the hash from the specified webpage.

        Returns:
            str: The hash of the webpage.
        """
        response = requests.get(self.url, auth=HTTPBasicAuth(
            env['SOEN6441_USERNAME'], 
            env['SOEN6441_PASSWORD']
        ))

        # Create hash of response webpage hexdigest
        return hashlib.sha256(response.text.encode('utf-8')).hexdigest()


    def monitor_webpage(self):
        """
        TODO:
        """

        # If no hash, get first hash and stop
        if self.last_hash is None:
            self.last_hash = self.get_hash()
            return
        else:
            # Get new hash
            new_hash = self.get_hash()

            # If new hash is different, print message and update last hash
            if new_hash != self.last_hash:
                # TODO: Send email
                pass