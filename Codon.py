import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


import random

bases = ['A', 'C', 'G', 'U']

# 生成4行5列的表格
mRNA = []
for _ in range(4):
    row = [random.choice(bases) for _ in range(5)]
    # 把前五列，两两相连
    for i in range(4):
        row.append(row[i] + row[i+1]) 
    mRNA.append(row)

# 打印表格
for row in mRNA:
    print('5\'-', ' '.join(row[:5]))

