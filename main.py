# Part of MyStreamListener in Main.ipynb
# Streaming With Tweepy
# Override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # Extract info from tweets
        id_str = status.id_str
        created_at = status.created_at
        user_created_at = status.user.created_at
        # ...... and more!
        # I'll talk about it below! (Or check full-code link above)
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits,
        stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            return False