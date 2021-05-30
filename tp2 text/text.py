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

"""
removing text file headers, footers
removing HTML, XML, etc. markup and metadata
extracting valuable data from other formats, such as JSON"""

sample = open('dataText.txt','r')
print(sample.readlines())

def strip_html(text):
    soup = BeautifulSoup(text, "html5lib")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    return text

final = denoise_text(sample)
print(final)

