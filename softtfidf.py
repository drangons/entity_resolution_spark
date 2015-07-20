"""
This module implements the soft tf-idf algorithm described in paper


This algorithm is best suited for record matching where the record is generally
smaller compared to document

Steps:
1. Load the data and compute the tf.idf score of document corpus
2. Score method return the soft tf-idf of the query against the record in the
corpus


"""

"""
Performance tips
"""

THRESHOLD = 0.9
CORPUS = ['cat ate food','dog like food']

import numpy as np
from  sklearn.feature_extraction.text import TfidfVectorizer
import jellyfish as jf
from collections import namedtuple

class Softtfidf():
    
    def __init__(self):
        tfidfvector = TfidfVectorizer(tokenizer=lambda x:x.split(" "))
   
    def buildcorpus(self):
        return tfidfvector.fit_transform(CORPUS)
        
    def builddict(self):
        matrix = builddcorpus()
        vocabulary = tfidfvector.vocabulary_
        tfidfdict ={}
        for docId,doc in enumerate(corpus):
            for word in doc.split(" "):
                tfidfdict[word]=matrix[(docId,vocabulary[word])]
    return tfidfdict
    
    def score(s,t):
        
        similar = namedtuple('Similar',['r1','r2','sim'])
        similarity=[]
        for i,ti in enumerate(s.split(" ")):
            for j,tj in enumerate(t.split(" ")):
                dist = jf.jaro_winkler(ti,tj)
                if dist >= THRESHOLD:
                    similarity.append(similar(i,j,
                                                 dist*tfidfdict[ti]*tfidfdict[tj]))
    
        similarity.sort(reverse=True,key=lambda x:x.sim)

        sused = np.array([False]*len(s),dtype=bool)
        tused = np.array([False]*len(t),dtype=bool)
    
    
        
        sim = 0.0
        for s in similarity:
            if(sused[s.r1] | tused[s.r2]):
                continue;
            sim+=s.sim
            sused[s.r1] = True
            tused[s.r2] = True
        return sim  
    
    
        


#matrix = tfidfvector.fit_transform(corpus).todense()

#tfidfvector.todense()

#features = tfidfvector.get_feature_names()

#vocabulary = tfidfvector.vocabulary_

def main(**kargs):
    """ Driver program """
    if data in kargs.keys():
        corpus=kargs[data]
    s=Softtfidf()
    for doc1,doc2 in zips(CORPUS,CORPUS):
        score = s.score()
        print(doc1,doc2,score)



if __name__ == '__main__':
    main()
