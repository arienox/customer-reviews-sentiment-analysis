##Load the data
import pandas as pd
df=pd.read_csv("C:/Users/ASUS/OneDrive/Documents/Python ML/sentiment analysis/customer_reviews.csv")
##nltk-natural language tool kit
import nltk
nltk.download("vader_lexicon") 
##call the function to analyse sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer
senti_analysis=SentimentIntensityAnalyzer()
##check sentiment of the first feedback
senti_analysis.polarity_scores(df.iloc[55,1])
print(df.iloc[55,1])
##check the sentiment of text
df["score"]=df["text"].apply(lambda x:senti_analysis.polarity_scores(x))
##extracting compound score
df["compound_score"]=df["score"].apply(lambda x:x["compound"])
print(df)
import numpy as np
df["positive_negative"]=df["compound_score"].apply(lambda x:np.where(x>0,"Positive","Negative"))
##count of negative and positive feedback
df["positive_negative"].value_counts()
positive_data=df.query("positive_negative=='Positive'")
print(positive_data)
