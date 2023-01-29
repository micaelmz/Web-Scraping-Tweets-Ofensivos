from twitter_scraper import TweetScraper
from data_manager import DataManager
import pandas as pd

MAX_TWEETS = 100


ts = TweetScraper()
dm = DataManager()

# if __name__ == '__main__':
#     term = dm.pick_a_term() # obsoleto
#     tweets_found = ts.scrape_tweets(dm.swear_list)
#     ts.put_into_dataframe()
#     data_csv = ts.tweets_df.to_csv(index=False)
#     dm.upload_to_google_sheet(csv=data_csv)
#     dm.send_email(info=term) # obsoleto
#     print(f"O data sheet foi atualizado com novos {tweets_found} tweets sobre a palavra {term['word'].upper()} da categoria {term['category'].upper()}")

#dm.clear_csv()

if __name__ == '__main__':
    dataset = dm.swear_list
    terms = {category: [word for word in dataset[category] if pd.notnull(word)] for category in dataset.columns.tolist()}

    for category in terms.keys():
        for word in terms[category]:
            list_of_tweets = ts.scrape_tweets(word, category)
            dm.upload_to_google_sheet(list_of_tweets)
            print(f"Termo {word} da categoria {category} foi coletado com sucesso!")
        print(f"Todos os termos da categoria {category} foram coletados com sucesso!")
    print(f"O data sheet foi atualizado com sucesso!")
#dm.clear_csv()
