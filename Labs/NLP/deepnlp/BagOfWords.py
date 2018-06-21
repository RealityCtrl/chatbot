#!/usr/bin/env python

#  Author: Angela Chapman
#  Date: 8/6/2014
#
#  This file contains code to accompany the Kaggle tutorial
#  "Deep learning goes to the movies".  The code in this file
#  is for Part 1 of the tutorial on Natural Language Processing.
#
# *************************************** #

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from Word2VecUtility import Word2VecUtility
import nltk
import pandas as pd
import numpy as np

if __name__ == '__main__':
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Sheet_2_train.csv'), header=0, quoting=3, usecols=['response_id','class','response_text'])
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Sheet_1.csv'), header=0, quoting=3, usecols=['response_id','response_text'], skiprows=range(2, 42), skipfooter=12 )

    #print ('The first review is:')
    #print (train["review"][0])

    #input("Press Enter to continue...")


    #print ('Download text data sets. If you already have NLTK datasets downloaded, just close the Python download window...')
    #nltk.download()  # Download text data sets, including stop words

    # Initialize an empty list to hold the clean reviews
    clean_train_reviews = []

    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list

    print ("Cleaning and parsing the training set movie reviews...\n")
    for i in range( 0, len(train["response_text"])):
        clean_train_reviews.append(" ".join(Word2VecUtility.review_to_wordlist(train["response_text"][i], True)))


    # ****** Create a bag of words from the training set
    #
    print ("Creating the bag of words...\n")


    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    train_data_features = vectorizer.fit_transform(clean_train_reviews)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    np.asarray(train_data_features)

    # Sum up the counts of each vocabulary word
    #dist = np.sum(train_data_features, axis=0)

    # print the vocab
    #vocab = vectorizer.get_feature_names()
    #print(vocab)


    # ******* Train a random forest using the bag of words
    #
    print ("Training the random forest (this may take a while)...")


    # Initialize a Random Forest classifier with 100 trees
    forest = RandomForestClassifier(n_estimators = 100)

    # Fit the forest to the training set, using the bag of words as
    # features and the sentiment labels as the response variable
    #
    # This may take a few minutes to run
    forest = forest.fit( train_data_features, train["class"] )



    # Create an empty list and append the clean reviews one by one
    clean_test_reviews = []

    print ("Cleaning and parsing the test set movie reviews...\n")
    for i in range(0,len(test["response_text"])):
        clean_test_reviews.append(" ".join(Word2VecUtility.review_to_wordlist(test["response_text"][i], True)))

    # Get a bag of words for the test set, and convert to a numpy array
    test_data_features = vectorizer.transform(clean_test_reviews)
    np.asarray(test_data_features)

    # Use the random forest to make sentiment label predictions
    print ("Predicting test labels...\n")
    result = forest.predict(test_data_features)

    # Copy the results to a pandas dataframe with an "id" column and
    # a "sentiment" column
    output = pd.DataFrame( data={"response_id":test["response_id"], "class":result} )

    # Use pandas to write the comma-separated output file
    output.to_csv(os.path.join(os.path.dirname(__file__), 'data', 'Bag_of_Words_model_2.csv'), index=False, quoting=3)
    print ("Wrote results to Bag_of_Words_model.csv")


