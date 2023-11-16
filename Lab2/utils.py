import nltk
import string as s
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import NLTKWordTokenizer
from bs4 import BeautifulSoup
import re

stop_words = stopwords.words("english")
stop_words.append('movi')
stop_words.append('film')
stop_words.append('charact')

tokenizer = NLTKWordTokenizer()
ps = PorterStemmer()

def remove_special_characters(text, remove_digits):
    if remove_digits:
        pattern=r'[^a-zA-Z\s]'
    else:
        pattern=r'[^a-zA-Z0-9\s]'
    text=re.sub(pattern,'',text)
    return text

stop_words = [remove_special_characters(i,True) for i in stop_words]

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def preprocess(text, remove_digits=True):
    # html tags and square brackets are gone
    text = strip_html(text)
    text = remove_between_square_brackets(text)

    # text is broken up to words and special characters and digits are gone
    tokens = tokenizer.tokenize(text)
    tokens = [remove_special_characters(i,remove_digits) for i in tokens if remove_special_characters(i,remove_digits)]
    
    # porter stemmer used to remove suffixes and normalize
    stems = [ps.stem(token) for token in tokens]

    # stop words like i, but, how etc. are removed
    stems = [i for i in stems if i not in stop_words]

    return stems