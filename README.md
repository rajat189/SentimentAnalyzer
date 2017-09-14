# SentimentAnalyzer

A Tool in Django for Visualisation of Sentiment Analysis of a topic from a live twitter stream.

![portfolio-1](https://user-images.githubusercontent.com/10284360/30446924-2b85ed36-99a8-11e7-845d-25872996468d.jpg)

## Install Requirement:

1. tweepy -- this moule is used to get twitter live streem for a topic
2. django -- this framework is used to develop a web based architechture.
3. textblob -- this module is used to find the polarity of a sentence.

## Deployment:

1. Create a clone of repositery using "git clone https://github.com/rajat189/SentimentAnalyzer.git" in console.
2. Requirements should be installed.
3. Get your access key for twitter api access. Paste keys in tweetUtil.py
4. Run this command to start the server in console "python manage.py runserver".

## Description

1. "SentimentAnalyzer/sentimentAnalyzer/util/" contains two main files regarding fetching tweets.

- **tweetUtil.py** contains twitter authenticatin with the api keys
- **sentimentDAO.py** contains the dao layer of model means all functionality related to fetching the data and clearing it from hash tags, urls etc.Then we are analysing the data with textblob to get the polarity of tweet. we are fetching 100 tweets. You can increase the limit but its good to keep it low.
2. In the output we used pie chart and line chart to analyze the negative, positive and neutral tweets.
3. Remaining files are common files for **django mvc pattern**.

