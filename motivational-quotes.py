import tweepy
import requests
import random
import schedule
import time

import os
from dotenv import load_dotenv

import pandas as pd

load_dotenv()

def main():
    api_key = os.getenv('api_key')
    api_key_secret = os.getenv('api_key_secret')
    access_token = os.getenv("access_token")
    access_token_secret = os.getenv("access_token_secret")
    url = "https://zenquotes.io/api/quotes/"
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    response = requests.get(url)
    data = response.json()
    
    list(data)
    
    ran= random.choice(data)
    
    print(ran['q'])
    

    api.update_status(ran['q'])



if __name__ == '__main__':
    

    schedule.every(5).minutes.do(main)
    
    while True:
        schedule.run_pending()
        time.sleep(5)

