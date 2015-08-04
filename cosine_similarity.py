# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:22:57 2015

@author: dikshith
"""

import numpy as np
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


'''
Simple example. Uses l2 normalization.
For spark implementation, refer entity resolution in spark.

Keep in mind - lower casing, lemma, stemming, charfilters, synonym expansion
from lucence.

Also additional analysis tools lile entity extraction.
'''
CORPUS=[
'cat is fun',
'dog is royal',
'pets are good friends']

tfidfvector0 = TfidfVectorizer(tokenizer=lambda x:x.split(" "))

tfidf_matrix0 =tfidfvector0.fit_transform(CORPUS)


doc=['friends are fun']

similarity = cosine_similarity(tfidfvector0.transform(doc),tfidf_matrix0)



print(similarity) #[[ 0.35955412  0.          0.57735027]]



print(tfidf_matrix0.todense())  # sparse vector representation, saves space

print(tfidfvector0.get_feature_names()) # features and the index in sparse vector


'''
Example two - word order doesn't matter. But spell error matter
'''
CORPUS = ['apocalypse now']
document = ['now apoclapse']


tfidfvector1 = TfidfVectorizer(tokenizer=lambda x:x.split(" "), norm = None)


tfidf_matrix1 = tfidfvector1.fit_transform(CORPUS)

print(tfidf_matrix1.todense())

docvec = tfidfvector1.transform(doc)

print(cosine_similarity(docvec,tfidf_matrix1)) # .70


'''
Eample three - n-gram 
Spell error can be corrected to some extent but blows up vector dimension.
Only suitable for short document like database text field
'''
CORPUS = ['apocalypse now']
document = ['now apoclapse']

tfidfvector2 = TfidfVectorizer(analyzer='char',norm=None, 
                               ngram_range=(2,3))
                    
tfidf_matrix2 = tfidfvector2.fit_transform(CORPUS)

print(tfidf_matrix2.todense())

print(tfidfvector2.get_feature_names())

print(cosine_similarity(docvec,tfidf_matrix2)) # 0.78