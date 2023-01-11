import pandas as pd
import requests
import os
import json

def connect_to_twitter():
    bearer_token = os.environ.get("BEARER_TOKEN")
    return {"Authorization": "Bearer {}".format(bearer_token)}
headers = connect_to_twitter()

def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent?query=ExtremeWeather"
    return requests.request("GET", url, headers=headers).json()
response = make_request(headers)
print(response)
