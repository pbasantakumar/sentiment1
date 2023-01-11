def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': 'ExtremeWeather'}
    return requests.request("GET", url, params=query_params,    headers=headers).json()
response = make_request(headers)
print(response)
