import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


import random

# 可选的字母
letters = ['A', 'C', 'G', 'U']

# 生成4行5列的表格
table = []
for _ in range(4):
    row = [random.choice(letters) for _ in range(5)]
    # 把前五列，两两相连
    for i in range(4):
        row.append(row[i] + row[i+1])  # 使用row而不是table
    table.append(row)

# 打印表格
for row in table:
    print(' '.join(row))
for row in table:
    print('5\'-', ' '.join(row[:5]))






# # 从CSV文件加载数据
# data = pd.read_csv('codon.csv')
#
# # 分离特征和目标
# rna_sequences = data.iloc[:, :5]  # RNA序列特征
# x_columns_indices = [5, 7, 9, 11]    # 目标（x，y）值
# x_values = data.iloc[:, x_columns_indices].values
# y_columns_indices = [6, 8, 10, 12]    # 目标（x，y）值
# y_values = data.iloc[:, y_columns_indices].values
#
#
# # 进行特征编码（独热编码）
# encoder = OneHotEncoder()
# rna_sequences_encoded = encoder.fit_transform(rna_sequences)
#
# # 将RNA序列的特征和目标值x、y作为输入
# X_train_rna, X_test_rna, y_train_x, y_test_x, y_train_y, y_test_y = train_test_split(rna_sequences_encoded, x_values, y_values, test_size=0.2, random_state=42)
#
# from sklearn.linear_model import LinearRegression
#
# # 创建线性回归模型
# model = LinearRegression()
#
# # 使用训练集数据拟合模型
# model.fit(X_train_rna, y_train_y)
#
# # 在测试集上进行预测
# y_pred = model.predict(X_test_rna)
#
#
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# mse = mean_squared_error(y_test_y, y_pred)
# mae = mean_absolute_error(y_test_y, y_pred)
# r2 = r2_score(y_test_y, y_pred)
#
# print("均方误差:", mse)
# print("平均绝对误差:", mae)
# print("决定系数:", r2)
#
#
# import numpy as np
#
# # 计算四个数的均值
# y_train_meanx = np.mean(y_train_x, axis=1)
# y_test_meanx = np.mean(y_test_x, axis=1)
#
# from sklearn.svm import SVR
# svm_model = SVR(kernel='rbf', C=2.0, epsilon=0.1)
# svm_model.fit(X_train_rna, y_train_meanx)
# y_pred = svm_model.predict(X_test_rna)
#
#
#
# mse = mean_squared_error(y_test_meanx, y_pred)
# mae = mean_absolute_error(y_test_meanx, y_pred)
# r2 = r2_score(y_test_meanx, y_pred)
#
# print("均方误差:", mse)
# print("平均绝对误差:", mae)
# print("决定系数:", r2)