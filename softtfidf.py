"""
Change Made
This module implements the soft tf-idf algorithm described in paper


This algorithm is best suited for record matching where the record is generally
smaller compared to document

Steps:
1. Compute the tf.idf score of document corpus
2. Score method return the soft tf-idf of the query against the record in the
corpus


"""

"""
Performance tips
"""

THRESHOLD = 0.9
#CORPUS = ['cat ate food','dog like food']
#CORPUS = ['apocalypse now']
CORPUS = []
import numpy as np
from  sklearn.feature_extraction.text import TfidfVectorizer
import jellyfish as jf
from collections import namedtuple

class Softtfidf():
    
    def __init__(self):
        self.tfidfvector = TfidfVectorizer(tokenizer=lambda x:x.split(" "))
   
    def buildcorpus(self):
        '''
        Returns sparse vector of tfidf score
        '''
        return self.tfidfvector.fit_transform(CORPUS)
        
    def builddict(self):
        '''
        Returns dictionary of words as key and tfidf score as value
        '''
        matrix = self.buildcorpus()
        vocabulary = self.tfidfvector.vocabulary_
        tfidfdict ={}
        for docId,doc in enumerate(CORPUS):
            for word in doc.split(" "):
                tfidfdict[word]=matrix[(docId,vocabulary[word])]
        return tfidfdict
    
    def score(self,s,t):
        '''
        Returns the similarity score
        '''
        similar = namedtuple('Similar',['r1','r2','sim'])
        similarity=[]
        tfidfdict = self.builddict()
        for i,ti in enumerate(s.split(" ")):
            for j,tj in enumerate(t.split(" ")):
                dist = jf.jaro_winkler(ti,tj)
                if dist >= THRESHOLD:
                    similarity.append(similar(i,j,
                                                 dist*tfidfdict.get(ti)* tfidfdict.get(tj)))
    
        similarity.sort(reverse=True,key=lambda x:x.sim)

        sused = np.array([False]*len(s),dtype=bool)
        tused = np.array([False]*len(t),dtype=bool)
    
    
        #check that the term are counted only once
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

def main():
    """ Driver program """
    #if data in kargs.keys():
    #    corpus=kargs[data]
    s=Softtfidf()
    document1 = 'apoclapse now'
    document2 = 'apocalypse now'
    CORPUS.append(document1)
    CORPUS.append(document2)
    print(s.score(document1,document2))
    #for doc1,doc2 in zip(CORPUS,CORPUS):
    #    score = s.score(doc1,doc2)
    #    print(doc1,doc2,score)



if __name__ == '__main__':
    main()
