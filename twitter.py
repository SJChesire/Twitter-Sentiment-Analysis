import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import re
import nltk
import nltk

data = pd.read_csv(r"C:\Users\HP 840\Desktop\Twitter sentiment analysis\twitter.csv")

print(data.head())

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import string

# Download the stopwords
nltk.download('stopwords')

# Initialize the stemmer
stemmer = nltk.SnowballStemmer("english")

# Set the stopwords
stopword = set(stopwords.words('english'))

def clean(text):
    text = str(text).lower()
    text = re.sub(r'\[.*?\]', '', text)  # Use raw string
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Use raw string
    text = re.sub(r'<.*?>+', '', text)  # Use raw string
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Use raw string
    text = re.sub(r'\n', '', text)  # Use raw string
    text = re.sub(r'\w*\d\w*', '', text)  # Use raw string
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text

# Assuming you have a DataFrame 'data' with a column 'tweet'
# Example of loading data from a CSV
data = pd.read_csv(r"C:\Users\HP 840\Desktop\Twitter sentiment analysis\twitter.csv")

# Apply the clean function to the 'tweet' column
data["tweet"] = data["tweet"].apply(clean)

# Check the cleaned data
print(data.head())

from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["tweet"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["tweet"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["tweet"]]

data = data[["tweet", "Positive", 
             "Negative", "Neutral"]]
print(data.head())

x = sum(data["Positive"])
y = sum(data["Negative"])
z = sum(data["Neutral"])

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print("Positive 😊 ")
    elif (b>a) and (b>c):
        print("Negative 😠 ")
    else:
        print("Neutral 🙂 ")
sentiment_score(x, y, z)

print("Positive: ", x)
print("Negative: ", y)
print("Neutral: ", z)