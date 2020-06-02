"""
Подготовка списка изображений тестовой выборкии.
Небходим файл Test.csv, предоставляемый с датасетом GTSRB
"""

import numpy as np
import pandas as pd


data = pd.read_csv('Test.csv')
x1 = data['Roi.X1'].values
y1 = data['Roi.Y1'].values
x2 = data['Roi.X2'].values
y2 = data['Roi.Y2'].values
class_id = data['ClassId'].values
path_names = data['Path'].values

X = np.array(list(zip(path_names,x1,y1,x2,y2, class_id)))

# Соответствие папок из исходного датасета к выбранным классам
# 0-0
# 1-27
# 2-29
# 3-37
# 4-39

f = open("test.txt", 'w')
#Выбор директории, содержащей файлы тестовой выборки
test_pattern = "/content/gdrive/My Drive/darknet/img/"

for i in range(0, len(X) - 1):
    if int(X[i][5])==0 or int(X[i][5])==27 or int(X[i][5])==29 or int(X[i][5])==37 or int(X[i][5])==39:
        f.write(test_pattern+X[i][0]+'\n')

f.close()


