import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing dataset and adding Custom values (defined by X & Y)
#: = selecting all the columns, :-1 == Selecting all the columns except the one,
# python indexes start from 0
dataset = pd.read_csv('Data.csv') #Data.csv as sample
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values   
 