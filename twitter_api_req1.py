def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent?query=ExtremeWeather"
    return requests.request("GET", url, headers=headers).json()
response = make_request(headers)
print(response)