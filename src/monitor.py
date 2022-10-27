# %%
import time
import hashlib
import requests
from email_client import EmailClient
from requests.auth import HTTPBasicAuth
import os

env = os.environ

class WebpageMonitor:
    """
    Monitors the webpage for changes by tracking the hash of the webpage.
    """
    def __init__(self, recipients:list, url='http://users.encs.concordia.ca/~cc/soen6441/', verbose=False) -> None:
        self.url = url
        self.frequency = 60
        self.last_hash = None
        self.verbose = verbose
        self.email_client = EmailClient(recipients, verbose=self.verbose)

    def __log(self, message):
        if self.verbose:
            print(f'LOG: {message}')

    def __get_hash(self):
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

    def __set_hash(self, new_hash):
        """
        Sets the hash of the webpage in the environment variables.
        """
        self.__log(f'Setting hash to {new_hash}')
        os.system(f'heroku config:set -a soen6441-bot LAST_HASH={new_hash}')
        self.last_hash = new_hash


    def monitor_webpage(self):
        """
        Monitors the hash of the webpage for changes.
        """
        new_hash = self.__get_hash()
        try:
            self.last_hash = env['LAST_HASH']
            # Get updated hash of webpage
            # If new hash is different, print message and update last hash
            if new_hash != self.last_hash:
                self.__log(f'Webpage change detected, sending email...')
                self.email_client.send_email(f'Webpage change detected at {self.url} at {time.ctime()}')
                self.__set_hash(new_hash)
                
            else:
                self.__log(f'No change detected at {time.ctime()}')
                
        except KeyError as _:
            # If last hash is not set, set it to the current hash
            self.__log('No website hash found in the environment variables. Setting hash...')
            self.__set_hash(new_hash)
            return