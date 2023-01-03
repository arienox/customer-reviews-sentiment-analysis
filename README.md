# Sentiment Analysis of Customer Reviews
This code is used to perform sentiment analysis on a dataset of customer reviews. It uses the SentimentIntensityAnalyzer function from the nltk library to analyze the sentiment of the text in the text column of the df dataframe. The function returns a dictionary of scores for different sentiments (positive, negative, neutral), with the compound score representing the overall sentiment of the text. The compound_score column is created by extracting the compound score from the dictionary, and the positive_negative column is created by applying a lambda function to the compound_score column that assigns the value "Positive" if the compound score is greater than 0 and "Negative" otherwise. The number of positive and negative reviews is then counted using the value_counts function. Finally, a new dataframe positive_data is created by filtering the original dataframe to only include rows with the value "Positive" in the positive_negative column.

## Getting Started
These instructions will guide you through the process of running this code on your local machine.

## Prerequisites
You will need to have the following libraries installed:
```
pandas
nltk
```
You can install these libraries by running the following command:

> pip install pandas nltk
## Running the code
1. Download the customer_reviews.csv file and place it in a directory on your local machine.
2. Open the sentiment_analysis.py file and update the file path for the customer_reviews.csv file to the correct file path on your machine.
3. Run the sentiment_analysis.py file.
## How the code works
1. The customer_reviews.csv file is loaded into a pandas dataframe.
2. The nltk library is imported and the vader_lexicon is downloaded.
3. The SentimentIntensityAnalyzer function from nltk is called to perform sentiment analysis on the review text.
4. A new column called "score" is added to the dataframe, which contains the sentiment scores for each review.
5. A new column called "compound_score" is added to the dataframe, which extracts the compound score from the "score" column.
6. A new column called "positive_negative" is added to the dataframe, which categorizes the review as positive or negative based on the compound score.
7. The value_counts function is used to count the number of positive and negative reviews.
8. A new dataframe called "positive_data" is created, which contains only the positive reviews.
## Results
The code will output the following:
```
The sentiment scores for the first review in the dataframe
The updated dataframe with the "score", "compound_score", and "positive_negative" columns
The count of positive and negative reviews
The dataframe containing only the positive reviews.
```
