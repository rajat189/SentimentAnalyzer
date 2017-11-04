import tweepy

consumer_key = "4vbbneEPjbSF5X4YUzoC3HKKK"
consumer_secret = "504qja1HTruv9QojzD6ittG03wtEGEzizT1ljsWT4w63LUBX2k"

access_token = "700561358727704576-tibiDsLIiJNugecJHulF88dsXiaKdiJ"
access_token_secret = "fEdpJitOZqeBwpH31j8sCBWl7PklOCWKZeC6MX7UDvNID"

class tweetData():

    def getTwitterData(self, tag):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            api=tweepy.API(auth)
            public_tweets=api.search( q = tag, count=100,language = 'en' )

            return public_tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


