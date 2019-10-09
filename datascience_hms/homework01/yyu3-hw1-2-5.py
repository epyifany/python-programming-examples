#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.stats import entropy

# Good for load small dataset
data = pd.read_csv('data-film.csv', encoding='utf-8', header=0)
f = open('data-film.csv', 'r')
lines = [line.strip('\n').split(',') for line in f][1:151]

# n is the number of samples
n = data['FILM_ID'].count()

# get list of features
f = open('data-film.csv', 'r')
features = [line.strip('\n').split(',') for line in f][0:1][0][1:5]

print(min(data[features[0]].tolist()))
print(max(data[features[0]].tolist()))

print(min(data[features[2]].tolist()))
print(max(data[features[2]].tolist()))

prob_website_1 = [0, 0, 0, 0]
prob_website_3 = [0, 0, 0, 0]
for film in lines:
#     four interval for website1 [4, 5), [5, 6), [6, 7), [7, 8]
    prob_website_1[int(float(film[1])) - 4] += 1

#     four interval for website3 [1, 2.5), [2.5, 4), [4, 5.5), [5.5, 7]
    prob_website_3[int((float(film[3]) - 1)/1.5)] += 1

for i in range(0,4):
    prob_website_1[i] /= 150.
    prob_website_3[i] /= 150.

print(entropy(prob_website_1, prob_website_3))
