import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


import random

bases = ['A', 'C', 'G', 'U']

# generate a 4*5 table
mRNA = []
for _ in range(4):
    row = [random.choice(bases) for _ in range(5)]
    # connect neighbour bases
    for i in range(4):
        row.append(row[i] + row[i+1]) 
    mRNA.append(row)

# Print the mRNA with KD
for row in mRNA:
    print('5\'-', ' '.join(row[:5]))

