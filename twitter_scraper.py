import snscrape.modules.twitter as sntwitter
import datetime as dt
import pandas as pd


class TweetScraper(object):
    """
    Essa classe é responsavel por lidar com o scraping de tweets.
    """

    def __init__(self):
        super().__init__()
        self.tweets_list = []  # lista de tweets
        self.tweets_df = pd.DataFrame()  # dataframe com os tweets
        self.MAX_TWEETS = -1

    def scrape_tweets(self, word, category):
        """
        Essa função é responsável por fazer o scraping de tweets, recebendo o termo e salvando o resultado na lista de tweets.
        """
        i = 0
        tweets_list = []
        today = dt.datetime.utcnow().date()
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(word+" lang:pt").get_items()):
            tweets_list.append([str(category), str(tweet.content), str(tweet.date), str(tweet.id), str(tweet.username), str(tweet.url), str(word)])
            if i > self.MAX_TWEETS:
                break
        return tweets_list

    def clear_list(self):
        """
        Essa função é responsável por limpar a lista de tweets.
        """
        self.tweets_list = []

    def put_into_dataframe(self):
        """
        Essa função é responsável por transformar a lista de tweets em um dataframe.
        """
        self.tweets_df = pd.DataFrame(self.tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Url', 'Word'])
        return self.tweets_df
