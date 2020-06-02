"""
ДЛЯ ТЕСТОВОЙ ВЫБОРКИ
Подготовка файлов с описанием рамки распознаваемого объекта.
Текстовые файлы содержат в себе номер соответствующего класса
и координаты рамок, ограничивающих объект интереса.
Данные о разметке берутся из файла Test.csv,
который предоставляется вместе с набором данных GTSRB.
Файл с разметкой расположить рядом со скриптом

Формат выходных данных:
class, x_0, y_0, x_1, y_1

"""
import os
import numpy as np
import pandas as pd


data = pd.read_csv('Test.csv')
x1 = data['Roi.X1'].values
y1 = data['Roi.Y1'].values
x2 = data['Roi.X2'].values
y2 = data['Roi.Y2'].values
class_id = data['ClassId'].values
path_names = data['Path'].values
width = data['Width'].values
heigth = data['Height'].values

X = np.array(list(zip(path_names,x1,y1,x2,y2, class_id,width,heigth)))

#Путь к папке, в которой будут хранится текстовые файлы
path = "./some_dir"
# list_dir = os.listdir(path)
os.chdir(path)

# Соответствие папок из исходного датасета к выбранным классам
# 0-0
# 1-27
# 2-29
# 3-37
# 4-39

class_name=""
tmp=""
for i in range(0,len(X)-1):
    if int(X[i][5]) == 0 or int(X[i][5]) == 27 or int(X[i][5]) == 29 or int(X[i][5]) == 37 or int(X[i][5]) == 39:
        tmp= X[i][0]
        tmp= tmp[5:-4]
        x_1 = str(float(X[i][1])/int(X[i][6]))
        y_1 = str(float(X[i][2])/int(X[i][7]))
        x_2 = str(float(X[i][3]) / int(X[i][6]))
        y_2 = str(float(X[i][4]) / int(X[i][7]))

        f = open(tmp+".txt",'w')
        if X[i][5]=='0':
            class_name='0'
        elif X[i][5]=='27':
            class_name='1'
        elif X[i][5]=='29':
            class_name='2'
        elif X[i][5]=='37':
            class_name='3'
        elif X[i][5]=='39':
            class_name='4'
        f.write(class_name+' '+x_1+' '+y_1+' '+x_2+' '+y_2)
        f.close()




