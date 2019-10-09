#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import math
import matplotlib.pyplot as plt

# Good for load small dataset
data = pd.read_csv('data-film.csv', encoding='utf-8', header=0)
f = open('data-film.csv', 'r')
lines = [line.strip('\n').split(',') for line in f][1:151]

# n is the number of samples
n = data['FILM_ID'].count()

# get list of features
f = open('data-film.csv', 'r')
features = [line.strip('\n').split(',') for line in f][0:1][0][1:5]


feature_no = 1 # starting point of feature labels

for feature in features:
    SUM = 0
    sum_of_diff_sq = 0
    Z_Score = []

    # find sample sum and sample mean
    for film in lines:
        SUM += float(film[feature_no])
    mean = SUM / n

    # find sample variance and standard deviation
    for film in lines:
        sum_of_diff_sq += (float(film[feature_no]) - mean) * (float(film[feature_no]) - mean)
#     print(sum_of_diff_sq)
    variance = sum_of_diff_sq / (n - 1)
    std_dev = math.sqrt(variance)


    # find min/max z score
    for film in lines:
        Z_Score.append(abs((float(film[feature_no]) - mean) / std_dev))
#         if MAX_Z_Score < abs((float(film[feature_no]) - mean) / std_dev):
#             MAX_Z_Score = abs((float(film[feature_no]) - mean) / std_dev)
    print(max(Z_Score))

    # proceed to the next feature
    feature_no = feature_no + 1
