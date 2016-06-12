import csv
def write_csv(tweets,screen_names):
    dict1 = {}
    for screen_name,tweet in zip(screen_names,tweets):
        dict1[screen_name] = tweet
        
    headers = dict1.keys()  
      
    with open("twitter.csv","w") as csvfile:
        tweet_writer = csv.writer(csvfile)
        tweet_writer.writerow(list(headers))
        tweet_writer.writerows(zip(*dict1.values()))

