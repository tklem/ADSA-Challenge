import csv as csv
import numpy as np
import pandas as pd

df = pd.read_csv('../ADSA_novice_training.csv',sep='/t',header=0)
train_array = df.as_Matrix()
                                 
data=[]                          
for row in train_array:      
    data.append(row)             
data = np.array(data) 	         