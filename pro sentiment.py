import pandas as pd
from afinn import Afinn

import re
import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lemmatizer import Lemmatizer
import nltk
from nltk import word_tokenize
import spacy
from tqdm import tqdm_notebook as tqdm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


nlp = spacy.load('en', disable=['parser', 'ner'])

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

def sentiment(dataframe):

    df = dataframe
    sentiment_scores = [None] * len(df)
    
    corpus = df.review
    
    cleaned_corpus = [None] * len(corpus)
    
    for i in tqdm(range(len(corpus)), leave = False):
        review = corpus[i].lower()
        review = re.sub(r'\d+', '', review)
        review = re.sub(r"[\(\),.;@#?!&$/*-]+\ *", " ", review)
        review = review.replace('\xa0', ' ')
        doc = nlp(review)
        lemma_review = " ".join([token.lemma_ for token in doc])
        tokens = word_tokenize(lemma_review)
        stopped_review = " ".join([i for i in tokens if not i in STOP_WORDS])
        cleaned_corpus[i] = stopped_review
        
    for i in range(len(cleaned_corpus)):
        sentiment_scores[i] = sentiment_analyzer_scores(cleaned_corpus[i])
        
    return sentiment_scores