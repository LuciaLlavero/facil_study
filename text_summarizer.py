import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import warnings
from nltk.corpus import stopwords

nltk.download('stopwords') 

HANDICAP = 0.85

def remove_punctuation_marks(text) :
    punctuation_marks = dict((ord(punctuation_mark), None) for punctuation_mark in string.punctuation)
    return text.translate(punctuation_marks)

def get_lemmatized_tokens(text) :
    normalized_tokens = nltk.word_tokenize(remove_punctuation_marks(text.lower()))
    return [nltk.stem.WordNetLemmatizer().lemmatize(normalized_token) for normalized_token in normalized_tokens]

def get_average(values) :
    greater_than_zero_count = total = 0
    for value in values :
        if value != 0 :
            greater_than_zero_count += 1
            total += value 
    return total / greater_than_zero_count

def get_threshold(tfidf_results) :
    i = total = 0
    while i < (tfidf_results.shape[0]) :
        total += get_average(tfidf_results[i, :].toarray()[0])
        i += 1
    return total / tfidf_results.shape[0]

def get_summary(documents, tfidf_results) :
    summary = ""
    i = 0
    while i < (tfidf_results.shape[0]) :
        if (get_average(tfidf_results[i, :].toarray()[0])) >= get_threshold(tfidf_results) * HANDICAP :
                summary += ' ' + documents[i]
        i += 1
    return summary

if __name__ == "__main__" :
    warnings.filterwarnings("ignore")

    try :
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print('punkt')
        nltk.download('punkt')

    try :
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')
    
    text = open('ai.txt', 'r').read()
    documents = nltk.sent_tokenize(text)

    tfidf_results = TfidfVectorizer(tokenizer = get_lemmatized_tokens, stop_words = stopwords.words('english')).fit_transform(documents)
    print (get_summary(documents, tfidf_results))
