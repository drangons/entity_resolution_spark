# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 06:53:30 2015

@author: dikshith

Levenshtein implementation
"""

import numpy as np

class Levenshtein:
    '''
    Implements levenshtein distance of two strings
    '''
    
    def __init__(self):
        pass
    
    def _computelevenshtein(self,s1,s2):
        slen = len(s1)
        tlen = len(s2)
        
        #matrix = np.zeros((slen+1,max(slen+1,tlen+1)))
        matrix = np.zeros((slen+1,tlen+1))
        
        #initalize
        for i in range(slen+1):
            matrix[i][0] = i
        
        for j in range(tlen+1):
            matrix[0][j] = j
            
        #print(matrix)
            
        for i in range(1,slen+1):
            for j in range(1,tlen+1):
                matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,
                                    matrix[i-1][j-1]+ (0 if s1[i-1] == s2[j-1]
                                    else 1))
                #print(matrix[i-1][j]+1,matrix[i][j-1]+1,
                                    #matrix[i-1][j-1]+ 0 if s1[i-1] == s2[j-1]
                                    #else 1)                    
        
        print("levendistance",matrix[slen][tlen]) 
        print(matrix)
        return matrix[slen][tlen]
        
    def score(self,s1,s2):
        return 1 - float(self._computelevenshtein(s1,s2))/max(len(s1),len(s2))


def main():
    l = Levenshtein()
    print(l.score('industry','interest'))

if __name__ == '__main__':
    main()
                
            