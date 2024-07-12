One social media site where users feel free to express their thoughts on any subject is Twitter now known as X.
On Twitter, we occasionally come into heated debates over people's opinions, which occasionally lead to an array of critical messages.
In light of this, this piece will teach you how to perform sentiment analysis on Twitter. 

 I have collected a dataset from Kaggle that contains tweets about a long discussion within a group of users.
 Here our task is to identify how many tweets are negative, neutral and positive so that we can give a conclusion.

 First, we start by importing the necessary Python libraries and Data sets
 Then, we need to prepare and clean up the data of errors and other special symbols because these tweets contain a lot of language errors.

 Now, the next step is to calculate the sentiment scores of these tweets and assign a label to the tweets as positive, negative, or neutral. Here is how you can calculate the sentiment scores of the tweets
 from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["tweet"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["tweet"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["tweet"]]

I will now limit my selection of this data to the columns required for the remaining Twitter sentiment analysis tasks.
data = data[["tweet", "Positive", 
             "Negative", "Neutral"]]
print(data.head())

We now have a look at the most frequent label assigned to the tweets according to the sentiment scores:

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

Most of the tweets are neutral. Now let’s have a look at the total of the sentiment scores:

print("Positive: ", x)
print("Negative: ", y)
print("Neutral: ", z)

The neutral tweets are way higher than negative and positive, but out of all the tweets, the negative tweets are more than the positive tweets, so we can say that most of the opinions are negative.
