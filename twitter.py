import tweepy
import get_tweets
import write_csv

auth = tweepy.OAuthHandler("qo0Fxvc8s8Coo20PRukvv1tFl", "AroPKZ8yTZyfuBEZ035Qo9iM4oNoEIwVYa5ItwFdi13UNRrHpr")
auth.set_access_token("3256502864-FjHx3f0lDVv5BalHzvEgYuM1Gx7nwt0TIYjNyDe", "CDioKATqsXZSvt2wxLoh3rB8G6uZqFGBaCjGZAl63yuSU")
api = tweepy.API(auth)


api = tweepy.API(auth)

screen_names = ["realDonaldTrump","HillaryClinton","imVkohli"]

tweet_persons = get_tweets.get_tweets(screen_names,api)

write_csv.write_csv(tweet_persons,screen_names)




