from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.sentiment.util import mark_negation
from nltk.corpus import stopwords
import string
import nltk


def overkill_tokenize(sentence):
    punt = list(string.punctuation)
    punt.remove("!")
    remove_words = stopwords.words('english') + punt
    sentence = sentence.lower()
    # first: tweet tokenize
    tweetTok = TweetTokenizer(strip_handles=True, reduce_len=True).tokenize
    lemma = WordNetLemmatizer().lemmatize
    preprocess_tweet = tweetTok(sentence)
    
    # second: lemmatization
    preprocess_tweetlemma = []
    for word in preprocess_tweet:
        if not word in remove_words:
            preprocess_tweetlemma.append(lemma(word))
    # third: add mark_negation
    preprocess_tweetLemmaMark = mark_negation(preprocess_tweetlemma)
    return preprocess_tweetLemmaMark
