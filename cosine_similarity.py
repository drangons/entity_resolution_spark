# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:22:57 2015

@author: dikshith
"""

import numpy as np
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CORPUS=[
'cat is fun',
'dog is royal',
'pets are good friends']

tfidfvector = TfidfVectorizer(tokenizer=lambda x:x.split(" "))

tfidf_matrix =tfidfvector.fit_transform(CORPUS)


doc=['friends are fun']

similarity = cosine_similarity(tfidfvector.transform(doc),tfidf_matrix)

print(similarity) #[[ 0.35955412  0.          0.57735027]]