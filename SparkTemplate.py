# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:31:17 2015

@author: dikshith
"""

'''
The template file for entity resolution in spark. 
Input1: File containing id,field1,field2 . Ex: 1,Toy Story 3,adventure
Input2: File containing id,field1,field2 . Ex: 222,Toz story III,adzenture
Output: File containg matching ids, Ex:1,222 if the two ids matching by fuzzing
comparing file1(field1) and file2(field1). simialrily for field2

 
Algorithm : We compare the corresponding fields in both fields using an 
algorithm. If the score of the comaprision is more than the threshold then we 
consider the fields are the same. If the score for field1 and field2 
comapriosions are above the threshold then we consider both the ids to be same.

Some of the algorithms that can be considered are
A. Charater based
1. Levenshtein 
2. Dameru-Levenshtein

B. Token based
1. Jaccard similarity
2. cosine similarity

C. Hybrid based
1. Soft Tf-idf
2. Monge-Eklan
   
'''
import re
from pyspark import SparkContext,SparkConf
from pyspark.sql import SqlContext,Row
import jellyfish as j
import csv

JARO_THRESHOLD =0.9
MONGE_THRESHOLD = 0.8

def preprocesing1(record):
    '''
    We have to preprocess field1 and field2 to elimante any character that
    doesn't contribute in the matching algorithm
    Ex: we are removing Non-alpha character here.
    Input : ('1','Toy Story-3','aDveNtUre')
    Output: Row(1,'toy story 3','adventure')
    '''
    id1, field1, field2 = record.tolower().split(",")
    field1 = re.sub(r'[-.\S_]+'," ",field1)
    
    return Row(int(id1),field1,field2)
    
def searchstratergy1(record1,record2):
    '''
    Input: Two strings
    Output: The similarity score if its above the threshold
    Example: Jaro-winkler with threshold 0.9
    '''
    
    score = j.jaro_winkler(record1, record2)
    if score >= JARO_THRESHOLD:
        return score
    else:
        return 0
        
def searchstratergy2(record1,record2):
    '''
    Input: Two strings
    Output: The similarity score if its above the threshold
    Example: Monge-Eklan with threshold 0.8
    '''
    
    score = monge_eklan(record1,record2)
    if score >= MONGE_THRESHOLD:
        return score
    else:
        return 0
         
def score(record):
    '''
    Input: Row(id1,field1,field2,id2,field11,field12)
    Output: Row(id1,id2,score)
    
    
    compares field1 and field11 with search strategy 1 and collects score1
    compare field2 and field12 with search stratergy 2 and collects score2
    
    score is the average of the score
    
    '''
    
    score1 = searchstrategy1(record.field1,record.field11)
    score2 = searchstratefy2(record.field2,record.field12)
    
    if score1 != 0 and score2 != 0:
        score = (score1+score2)/2
        return Row((id1,id2),score)
        

def main():
    #intial configuration
    conf = SparkConf().setAppName("Entity resolution").setMaster(master)
    sc = SparkContext(conf=conf)
    
    #read input files
    input1 = sc.textFile('Path to input 1').map(preprocessing1)
    input2 = sc.textFile('Path to input2').map(preprocessing2)
    
    # catersian product returens [((id1,field1,field2),(id11,field11,field12)),]    
    #convert it to [(id1,id11,field1,field11,field2,field12),....]
    crossprod = input1.cartesian(input2).map(tranformrecord)
    
    #collect the results
    results = crossprod.map(score).collect()
    
    header = ['id1','id2','avgscore']
    
    #write the output
    with open('ids.txt','wb') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for record in results:
            writer.writerow('{},{},{}'.format(record[0],record[1],record[2]))
        
    
if __name__ == '__main__':
    main()
        
    
    
    
        
    
    
    
    
    
    

    