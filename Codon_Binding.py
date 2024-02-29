
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from scipy.sparse import hstack
import pandas as pd

codon = pd.read_csv('/Users/Meng/Desktop/codon.csv')


def manipulate_dataframe(datafunc):
    datafunc = pd.DataFrame(datafunc)
    datafunc.insert(5, '12', 'data')
    datafunc['12'] = datafunc.iloc[:, 0] + datafunc.iloc[:, 1]
    datafunc.insert(6, '23', 'data')
    datafunc['23'] = datafunc.iloc[:, 1] + datafunc.iloc[:, 2]
    datafunc.insert(7, '34', 'data')
    datafunc['34'] = datafunc.iloc[:, 2] + datafunc.iloc[:, 3]
    datafunc.insert(8, '45', 'data')
    datafunc['45'] = datafunc.iloc[:, 3] + datafunc.iloc[:, 4]

    copied_data = datafunc.iloc[:, 5:9]
    for i in range(9, 22, 4):
        datafunc = pd.concat([datafunc.iloc[:, :i], copied_data, datafunc.iloc[:, i:]], axis=1)

    replacement_dictG = {
        'AA': -0.93,
        'UU': -0.93,
        'AU': -1.10,
        'UA': -1.33,
        'CU': -2.08,
        'AG': -2.08,
        'CA': -2.11,
        'UG': -2.11,
        'GU': -2.24,
        'AC': -2.24,
        'GA': -2.35,
        'UC': -2.35,
        'CG': -2.36,
        'GG': -3.26,
        'CC': -3.26,
        'GC': -3.42
    }

    replacement_dictH = {
        'AA': -6.82,
        'UU': -6.82,
        'AU': -9.38,
        'UA': -7.69,
        'CU': -10.48,
        'AG': -10.48,
        'CA': -10.44,
        'UG': -10.44,
        'GU': -10.40,
        'AC': -10.40,
        'GA': -12.44,
        'UC': -12.44,
        'CG': -10.64,
        'GG': -13.39,
        'CC': -13.39,
        'GC': -14.88
    }

    replacement_dictS = {
        'AA': -19.0,
        'UU': -19.0,
        'AU': -26.7,
        'UA': -20.5,
        'CU': -27.1,
        'AG': -27.1,
        'CA': -26.9,
        'UG': -26.9,
        'GU': -29.5,
        'AC': -29.5,
        'GA': -32.5,
        'UC': -32.5,
        'CG': -26.7,
        'GG': -32.7,
        'CC': -32.7,
        'GC': -36.9
    }

    replacement_dictSt = {
        'AA': -5.37,
        'UU': -5.37,
        'AU': -6.57,
        'UA': -3.82,
        'CU': -6.78,
        'AG': -6.78,
        'CA': -6.57,
        'UG': -6.57,
        'GU': -10.51,
        'AC': -10.51,
        'GA': -9.81,
        'UC': -9.81,
        'CG': -9.61,
        'GG': -8.26,
        'CC': -8.26,
        'GC': -14.59
    }

    replacement_dictWC = {
        'AA': 26,
        'UU': 26,
        'AU': 26,
        'UA': 26,
        'CU': 34,
        'AG': 34,
        'CA': 34,
        'UG': 34,
        'GU': 34,
        'AC': 34,
        'GA': 34,
        'UC': 34,
        'CG': 42,
        'GG': 42,
        'CC': 42,
        'GC': 42
    }

    datafunc.iloc[:, 5:9] = datafunc.iloc[:, 5:9].replace(replacement_dictG)
    datafunc.iloc[:, 9:13] = datafunc.iloc[:, 9:13].replace(replacement_dictH)
    datafunc.iloc[:, 13:17] = datafunc.iloc[:, 13:17].replace(replacement_dictS)
    datafunc.iloc[:, 17:21] = datafunc.iloc[:, 17:21].replace(replacement_dictSt)
    datafunc.iloc[:, 21:25] = datafunc.iloc[:, 21:25].replace(replacement_dictWC)

    return datafunc

# print(data.head())

data = manipulate_dataframe(codon)
rna_sequences = data.iloc[:, :5]  # RNA序列特征
targets = data.iloc[:, 25:26]        # 目标（x，y）值
# print(targets)

# 进行特征编码（独热编码）
encoder = OneHotEncoder()
rna_sequences_encoded = encoder.fit_transform(rna_sequences)
# X_train, X_test, y_train, y_test = train_test_split(rna_sequences_encoded, targets, test_size=0.2, random_state=42)

additional_dataG = data.iloc[:, 5:9]
additional_dataH = data.iloc[:, 9:13]
additional_dataS = data.iloc[:, 13:17]
additional_dataSt = data.iloc[:, 17:21]
additional_dataWC = data.iloc[:, 21:25]
# X_train_concatenated1 = hstack([rna_sequences_encoded, additional_dataWC])
# X_train_concatenated2 = hstack([rna_sequences_encoded, additional_dataG, additional_dataWC])
X_train_concatenated3= hstack([rna_sequences_encoded, additional_dataWC])
X_train, X_test, y_train, y_test = train_test_split(X_train_concatenated3, targets, test_size=0.20, random_state=42)


y_train = y_train.values.ravel()
y_test = y_test.values.ravel()


# LR
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# SVR
# from sklearn.svm import SVR
# svm_regressor = SVR(kernel='linear')
# # svm_regressor = SVR(kernel='poly', degree=3)
# # svm_regressor = SVR(kernel='rbf', C=1.0, epsilon=0.1)
# svm_regressor.fit(X_train, y_train)
# y_pred = svm_regressor.predict(X_test)

# RFR
# from sklearn.ensemble import RandomForestRegressor
# random_forest_regressor = RandomForestRegressor(n_estimators=60, random_state=42)  # 设置100棵决策树
# random_forest_regressor.fit(X_train, y_train)
# y_pred = random_forest_regressor.predict(X_test)

# GBR
from sklearn.ensemble import GradientBoostingRegressor
gb_regressor = GradientBoostingRegressor(n_estimators=60, learning_rate=0.1, max_depth=4, random_state=42)
gb_regressor.fit(X_train, y_train)
y_pred = gb_regressor.predict(X_test)



# 计算模型的评估指标
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# mse = mean_squared_error(y_test, y_pred)
# mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# print("Mean Squared Error:", mse)
# print("Mean Absolute Error:", mae)
print("R^2 Score:", r2)

# intercept = model.intercept_
# coefficients = model.coef_
#
# print("Intercept (截距):", intercept)
# print("Coefficients (系数):", coefficients)


import itertools

bases = ['A', 'C', 'G', 'U']
all_sequences = list(itertools.product(bases, repeat=5))
mRNA = [list(seq) for seq in all_sequences]

mRNA_df = pd.DataFrame(mRNA, columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])


# import random
# bases = ['A', 'C', 'G', 'U']
# mRNA = []
# for _ in range(20):
#     row = [random.choice(bases) for _ in range(5)]
#     # connect neighbour bases
#     for i in range(4):
#         row.append(row[i] + row[i+1])
#     mRNA.append(row)


extra = manipulate_dataframe(mRNA_df)

rna_sequences_extra = extra.iloc[:, :5]
encoder = OneHotEncoder()
rna_sequences_encoded_extra = encoder.fit_transform(rna_sequences_extra)

additional_data_extraWC = extra.iloc[:, 21:25]
X_extra = hstack([rna_sequences_encoded_extra, additional_data_extraWC])
y_extra = gb_regressor.predict(X_extra)

import numpy as np
def transform_y(y_values):
    transformed_y = []
    for y_value in y_values:
        if y_value < 1:
            transformed_y.append("<1")
        elif 1 <= y_value < 10:
            transformed_y.append(round(y_value, 1))
        elif 10 <= y_value < 50:
            transformed_y.append(round(y_value))
        elif 50 <= y_value < 150:
            transformed_y.append(round(y_value / 5) * 5)
        elif 150 <= y_value < 1000:
            transformed_y.append(round(y_value / 10) * 10)
        else:
            transformed_y.append(">1000")

    return transformed_y

y_extra_trans = transform_y(y_extra)
#
# # Print the mRNA with KD
# for row, pred in zip(mRNA, y_extra_trans):
#     print('5\'-', ' '.join(row[:5]), pred)

import csv

output_file = 'extra_codon.csv'

# 打开CSV文件进行写操作
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # 写入标题行
    writer.writerow(['RNA Sequence', 'Prediction KD'])

    # 将结果写入CSV文件
    for row, pred in zip(mRNA, y_extra_trans):
        sequence = '5\'-' + ' '.join(row[:5])
        writer.writerow([sequence, pred])