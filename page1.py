import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# from google.colab import files
# uploaded = files.upload()
# coonect as OATH jump server
consumer_key = "UgSlsnLVlvWsAZjebUdzwXlT6"
consumer_sec = "isJC9mfe85shl0Pch6uofjDgGfPeQdTPN8c4KNCWrC0RwNH7jt"

# from proxy server we need to connect
access_token = "470819711-Yo7Nw3Rebmv1MB6n5qMdRTpqPqlz0KCsYVDbZkcQ"
access_token_sec = "m1dBkLTfnNXeNF6onBXhItUep8BIQjxl5Be2OkaEv2Sdu"
# connect to jump server of twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_sec)

# now we can connect from jump server to webserver of twitter
auth.set_access_token(access_token, access_token_sec)

# now we can connect to API strong server of twitter
api_connect = tweepy.API(auth)

posts = api_connect.user_timeline(screen_name="BillGates", count=10, tweet_mode="extended")
print("show the recent 5 tweets: \n")
i = 1
for tweet in posts[0:5]:
    print(str(i) + ') ' + tweet.full_text + '\n')
    i = i + 1

    # Create a dataframe with a column called Tweets
    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
    df.head()

print("show the recent 6 tweets: \n")


# Clean the text function
def cleanTxt(text):
    print("Inside cleantext: \n")
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Remove @mentioned
    text = re.sub(r'#', '', text)  # Remove the # symbol
    text = re.sub(r'RT[\s]+', '', text)  # Remove RT
    text = re.sub(r'https?:\/\/\s+', '', text)  # Removing hyperlink
    return text


print("show the recent 7 tweets: \n")
# cleaning the text
df['Tweets'] = df['Tweets'].apply(cleanTxt)
# show the clean text
print("show the recent 8 tweets: \n")
df
print("show the recent 9 tweets: \n")