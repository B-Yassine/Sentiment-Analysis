from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = "JFCpBNeLhi58xX3iJUBz7GrtT"
consumerSecret = "aCr1MUQpebTGztcyypmaJajzQCFzitqrMslyAmomN4PEbfUkNa"
accessToken = "1048553227061551104-zfzMOklc4nGGtclUJk7OfYfS7OyaYs"
accessTokenSecret = "zJzm3dPTTCRhrLYgUs2YoO2654fEgPeHyUi2FcZXxQs6K"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Entrer Keyword/Hashtag a chercher: ")
noOfSearchTerms = int(input("Entrer combien de tweets a analyser: "))

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

print("Comment les gens reagis sur "+searchTerm+" on analysons "+str(noOfSearchTerms)+" tweets: ")

if(neutral > positive and neutral > negative):
    print("Neutral")
elif(positive > neutral and positive > negative):
    print("Negative")
elif(negative > positive and negative > neutral):
    print("positive")

labels = ['Positive ['+str(positive)+' %]', 'Negative ['+str(negative)+' %]', 'Neutral ['+str(neutral)+' %]']
sizes = [positive, negative, neutral]
colors = ['red', 'blue', 'green']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc='best')
plt.title("Comment les gens reagis sur "+searchTerm+" on analysons "+str(noOfSearchTerms)+" tweets: ")
plt.axis('equal')
plt.tight_layout()
plt.show()
