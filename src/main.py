# %%
import time
import hashlib
import requests
from requests.auth import HTTPBasicAuth
import os

env = os.environ

url = 'http://users.encs.concordia.ca/~cc/soen6441/'

response = requests.get(url, auth=HTTPBasicAuth(
    env['SOEN6441_USERNAME'], 
    env['SOEN6441_PASSWORD']
))
# %%
