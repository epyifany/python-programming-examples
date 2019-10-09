#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import sys

# Good for load small dataset
data = pd.read_csv('data-film.csv', encoding='utf-8', header=0)
f = open('data-film.csv', 'r')
lines = [line.strip('\n').split(',') for line in f][1:151]

# n is the number of samples
n = data['FILM_ID'].count()

# get list of features
f = open('data-film.csv', 'r')
features = [line.strip('\n').split(',') for line in f][0:1][0][1:6]

GENRES = data[features[4]].unique().tolist()

GENRE_NO = 0
GENRE_RATING_MEAN = []

for GENRE in GENRES:
    GENRE_COUNT = 0
    GENRE_RATING_SUM = 0

    for film in lines:
        if film[5] == GENRE:
            GENRE_COUNT += 1
            GENRE_RATING_SUM += float(film[1])
    GENRE_RATING_MEAN.append(GENRE_RATING_SUM / GENRE_COUNT)
    GENRE_NO += 1

plt.figure()

y_pos = np.arange(len(GENRES))
plt.bar(y_pos, GENRE_RATING_MEAN)
plt.xticks(y_pos, GENRES)
plt.ylabel('Ratings')
plt.title("Bar Chart of " + features[0])
plt.show()
