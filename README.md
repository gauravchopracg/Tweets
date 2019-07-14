# Tweets-Analyzer

This is the code for the Analysis of tweets. I have divided the task of analysis into two parts; in first part, analyzing sentiment of tweets and see if it is positive or negative. In second part, we extract information from from a specific username handle and then form a csv file which contain favourite count, retweet count and image count. The code uses the [tweepy](http://www.tweepy.org/)  library to access the Twitter API and the [TextBlob](https://textblob.readthedocs.io/en/dev/) library to perform Sentiment Analysis on each Tweet. We will also be using numpy, pandas and json for data manipulation.

## Dependencies

* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)

## Usage

Once you have your dependencies installed via pip, run the script in terminal via

```
python sentiment.py
python tweets.py
```
