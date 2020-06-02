"""
Подготовка списка изображений обучающей выборкии.

"""
import os

# путь до папки с изображениями обучающей выборки
path = "./some_dir/Train/39/"
list_dir = os.listdir(path)
os.chdir(path)

# Соответствие папок из исходного датасета к выбранным классам
# 0-0
# 1-27
# 2-29
# 3-37
# 4-39

f = open("train.txt", 'a')
train_pattern = "/content/gdrive/My Drive/darknet/img/Train/4/"

for file in list_dir:
    f.write(train_pattern + file +"\n")

f.close()