# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:21:41 2021

@author: ASUS
"""


import re, string, unicodedata
import nltk
import inflect

from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk import FreqDist

"""
removing text file headers, footers
removing HTML, XML, etc. markup and metadata
extracting valuable data from other formats, such as JSON"""


# deruire l html
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


# supprimes tous les varraibles entre les brakets 
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

    
    
# pour mettre les les chars on lowercase
def toLower(text):
    lower_text = text.lower()
    return lower_text 



# supprime tous les noms sinificatif
def sotp_removale_words(text):
    stopword = stopwords.words('english')
    return stopword



# sparer les mots sous-forme des tokens, et trouver les origines des mots
def lemmatizer(text):
    word_tokens = text
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
    return lemmatized_word


# comptes les frequens mots dans le text
def count_frequent_word(text):
    freq = FreqDist(text)
    return (freq.most_common(5))

# remplacer tous les nombre en lettre
def replace_numbers(text):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    word_tokens = nltk.word_tokenize(text)
    p = inflect.engine()
    new_words = []
    for word in word_tokens:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

# convertire list de text en text
def toText(text):
    ss = ""
    for word in text:
        ss += word+" "
    return ss

input = open('dataText.txt').read()

strip_html=strip_html(input)
rm = remove_between_square_brackets(strip_html)
lower_text = toLower(rm)

remove_brakets = remove_between_square_brackets(lower_text)

replace_numbers = replace_numbers(remove_brakets)
text = nltk.Text(replace_numbers)
mostFreq=count_frequent_word(text)
lemmatizer = lemmatizer(replace_numbers)
print(lemmatizer)
sample = sotp_removale_words(lemmatizer)
text = toText(lemmatizer)

