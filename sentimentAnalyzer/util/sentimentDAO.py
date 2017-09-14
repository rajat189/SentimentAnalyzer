import re
from textblob import TextBlob
from sentimentAnalyzer.util.tweetUtil import tweetData

class Analysis():
    def filterTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyzedData(self,tag):

        fetcher=tweetData()
        listData=fetcher.getTwitterData(tag)

        tweetList=[]
        pos=0
        neg=0
        nut=0
        outPut=[]

        if len(listData)>0:
            for tweet in listData:
                tweetDict={}

                analysis=TextBlob(self.filterTweet(tweet.text))

                pol=float("{0:.2f}".format(analysis.sentiment.polarity))

                if pol<0:
                    neg+=1
                elif pol>0:
                    pos+=1
                else:
                    nut+=1

                tweetDict['tweet']=tweet.text
                tweetDict['user']=tweet.user.screen_name
                tweetDict['polarity']=pol

                tweetList.append(tweetDict)

        total=pos+neg+nut
        if total==0:
            nut=1
            total=1

        pos=float("{0:.2f}".format((pos/total)*100))
        neg=float("{0:.2f}".format((neg/total)*100))
        nut=float("{0:.2f}".format((nut/total)*100))

        outPut.append(nut)
        outPut.append(pos)
        outPut.append(neg)

        return {'tweet_list': tweetList, 'pie_list': outPut, 'count': total}
