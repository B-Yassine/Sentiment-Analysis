from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = "XXXXXXXXXXXXXXXXXXXXX"
consumerSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
accessToken = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
accessTokenSecret = "XXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter Keyword/Hashtag to analyse: ")
noOfSearchTerms = int(input("Enter how many tweets of your Keyword/Hashtag to analyse: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people react to "+searchTerm+", by analyzing "+str(noOfSearchTerms)+" tweets: ")

if(neutral > positive and neutral > negative):
    print("Neutral")
elif(positive > neutral and positive > negative):
    print("Positive")
elif(negative > positive and negative > neutral):
    print("Negative")

labels = ['Positive ['+str(positive)+' %]', 'Negative ['+str(negative)+' %]', 'Neutral ['+str(neutral)+' %]']
sizes = [positive, negative, neutral]
colors = ['red', 'blue', 'green']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc='best')
plt.title("How people react to "+searchTerm+", by analyzing "+str(noOfSearchTerms)+" tweets: ")
plt.axis('equal')
plt.tight_layout()
plt.show()
