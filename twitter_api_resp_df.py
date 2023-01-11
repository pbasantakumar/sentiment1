def make_df(response):
    return pd.DataFrame(response['data'])
df = make_df(response)
df