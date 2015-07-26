# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 04:59:06 2015

@author: dikshith

Implementation of Monge-Eklan algorithm.
Using Jaro-winkler as inner similarity function. 
you can use levenshtein or jaro distance as well.
"""

import jellyfish as j

class MongeEklan():
    '''
    Accepts the inner similarity function
    '''
    def __init__(self):
        pass
    
    def score(self,s,t):
        '''
        Input: s - multi-word string
               t - multi-word string
        Output : score
        Note: In single word string, score = jaro-winkler score
        '''
        cummax = 0
        
        for ws in s.split(" "):
            maxscore=0
            for wt in t.split(" "):
                maxscore = max(maxscore,j.jaro_winkler(ws,wt))
                #print(maxscore,"--",ws,"--",wt)
            cummax += maxscore
        
        return cummax/len(s.split(" "))
        
def main():
    m = MongeEklan()
    print(m.score("peter christen","christian pedro"))
    print(m.score("paul johnson","johson paule"))
    
if __name__ == '__main__':
    main()