#from model.Trainer import MuseGANTrainer
#from data.dataset import get_song_condition
import torch
import numpy as np

data = np.load("data/chord_sequence/tra/x_bar_chroma.npy")
target = np.load("data/chord_sequence/tra/y_bar_chroma.npy")
data = data.transpose([0,3,1,2])
target = target.transpose([0,3,1,2])
print(data.shape)
print(target.shape)

cnt_out = 0
cnt_four = 0
min = 99
max = 0

for i in range(target.shape[0]):
    for j in range(target.shape[2]):
        for k in range(target.shape[3]):
            if target[i][0][j][k] == True:
                if k < min:
                    min = k
                if k > max:
                    max = k

        print("min is:",min)
        print("max is:",max)

for i in range(target.shape[0]):
    for j in range(target.shape[2]):
        cnt_chroma = 0
        for k in range(target.shape[3]):
            if target[i][0][j][k] == True:
                cnt_chroma += 1

        if cnt_chroma>=4:
            cnt_four += 1

print("cnt_out is:", cnt_out)
print("max is:", max)
print("min is:", min)
print("cnt_four is", cnt_four)