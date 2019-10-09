#!/usr/bin/env python
# coding: utf-8

import pandas as pd
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

plt.figure()
plt.boxplot(data[features[0]].tolist())
plt.title("Boxplot of AVGRATING_WEBSITE_1")
plt.show()
