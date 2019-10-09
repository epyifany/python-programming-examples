#!/usr/bin/env python

import pandas as pd
import math
import matplotlib.pyplot as plt
import pandas as pd


col_names = ['ID',
 'Date',
 'Opponent',
 'Is_Home_or_Away',
 'Is_Opponent_in_AP25_Preseason',
 'Media',
 'Label']
# load dataset
pima = pd.read_csv("Dataset-football-train.csv", header=None,names=col_names)
# pima.head()

set_names = []
data = pima[1:]
print(data)
data_list = []
for feature in col_names:
    value_list = []
    feature_value_set= set()
    for data_value in data[feature]:
        feature_value_set.add(data_value)
    feature_value_list = list(feature_value_set)
    print(feature_value_list)
    set_names.append(feature_value_list)
    for data_value in data[feature]:
        value_list.append(feature_value_list.index(data_value))
    data_list.append(value_list)



# homeaway
print(data_list[3])

#top25
print(data_list[4])

#media
print(data_list[5])

list_of_wins = []

for j in range (3,5):
    win_prob = [0,0]
    lose_prob = [0,0]
    for i in range(0, len(data_list[6])):

        if data_list[6][i] is 0:
            win_prob[data_list[j][i]] += 1
        if data_list[6][i] is 1:
            lose_prob[data_list[j][i]] += 1
    print(win_prob)
    print(lose_prob)

j = 5
win_prob = [0,0,0,0,0]
lose_prob = [0,0,0,0,0]
for i in range(0, len(data_list[6])):
    if data_list[6][i] is 0:
        win_prob[data_list[j][i]] += 1
    if data_list[6][i] is 1:
        lose_prob[data_list[j][i]] += 1
print(win_prob)
print(lose_prob)

wl = ["win","loss"]
ha=['Home', 'Away']
io=['In', 'Out']
mda=['FOX', 'ABC', 'CBS', 'ESPN', 'NBC']

homeaway = [[5/7, 2/7],[1/2, 1/2]]
inout = [[1/7, 6/7],[1/2, 1/2]]
media = [[0, 3/14,0,1/14,10/14],[1/10, 4/10,1/10,0,4/10]]

# for i in range(0,2):
#     for j in range(0,5):
#         for k in range(0,2):
#             for l in range(0,2):
#                 print("wl is", i)
#                 print("jmedia is", j)
#                 print("homeaway is", k)
#                 print("inout is", l)
#                 print("prob of "+wl[i]+" in "+mda[j]+ha[k]+io[l]+" is", homeaway[i][k]*inout[i][l]*media[i][j])


for j in range(0,5):
    for k in range(0,2):
        for l in range(0,2):
#                 print("wl is", i)
#                 print("jmedia is", j)
#                 print("homeaway is", k)
#                 print("inout is", l)
#             a = homeaway[0][k]*inout[0][l]*media[0][j]
#             b
            if homeaway[0][k]*inout[0][l]*media[0][j] > homeaway[1][k]*inout[1][l]*media[1][j]:
                print("prediction of "+mda[j]+ha[k]+io[l]+" is win")
            else:
                print("prediction of "+mda[j]+ha[k]+io[l]+" is loss")
