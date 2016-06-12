def get_tweets(screen_names,api):
    tweet_person = []
    for name in screen_names:
        tweet_list = api.user_timeline(screen_name=name,count=100)
        tweet_text = []
        for item in tweet_list:
            tweet_text.append(item.text)
        tweet_person.append(tweet_text)
    return tweet_person
