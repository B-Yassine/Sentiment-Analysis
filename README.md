# Sentiment-Analysis
Sentiment Analysis on some tweets using the Twitter API in Python with Tweepy and TextBlob 

# Installation:
Tweepy: Twitter library for python.

    pip install tweepy
    
TextBlob: TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

    pip install textblob
    
# Authentication:
In order to fetch tweets through Twitter API, one needs to register an App through their twitter account:

    Open: https://apps.twitter.com/ and click the button: ‘Create New App’
    Fill the application details. You can leave the callback url field empty.
    Once the app is created, you will be redirected to the app page.
    Open the ‘Keys and Access Tokens’ tab.
    Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.


# Finally:
Parse the tweets. Classify each tweet as positive, negative or neutral and visualize it using matplotlib Pie Chart
