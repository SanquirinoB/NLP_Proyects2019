from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.sentiment.util import mark_negation


def overkill_tokenize(sentence):
    # first: tweet tokenize
    tweetTok = TweetTokenizer(strip_handles=True, reduce_len=False).tokenize
    lemma = WordNetLemmatizer().lemmatize
    preprocess_tweet = tweetTok(sentence)
    # second: lemmatization
    preprocess_tweetlemma = []
    for word in preprocess_tweet:
        preprocess_tweetlemma.append(lemma(word))
    # third: add mark_negation
    preprocess_tweetLemmaMark = mark_negation(preprocess_tweetlemma)
    return preprocess_tweetLemmaMark
