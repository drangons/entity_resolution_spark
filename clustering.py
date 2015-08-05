# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:55:35 2015

@author: dikshith
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re 


df = pd.read_csv(r'./measurements.csv',
            sep=';',header=0)
            
df.head()

df = df.map(lambda x : re.sub(",",".",x))


# count the number of zeros
np.count_nonzero(np.isnan(p6315))
