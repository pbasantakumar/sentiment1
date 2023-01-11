def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': 'ExtremeWeather -is:retweet',
    'start_time': "2021–10–03T00:00:00.000Z",
    'start_time': "2021–10–03T23:59:00.000Z",
    'max_results': 15,
    'tweet.fields': 'id,text,geo,conversation_id,created_at',
    'user.fields': 'id,name,username,location',
    'place.fields': 'full_name,country',
    'next_token': {}}
    return requests.request("GET", url, params=query_params, headers=headers).json()
response = make_request(headers)
print(response)