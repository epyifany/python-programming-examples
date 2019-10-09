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

ACTION_RATING_1 = []
ACTION_RATING_3 = []
ROMANCE_RATING_1 = []
ROMANCE_RATING_3 = []
COMEDY_RATING_1 = []
COMEDY_RATING_3 = []

for film in lines:
    if film[5] == "ACTION":
        ACTION_RATING_1.append(float(film[1]))
        ACTION_RATING_3.append(float(film[3]))
    if film[5] == "ROMANCE":
        ROMANCE_RATING_1.append(float(film[1]))
        ROMANCE_RATING_3.append(float(film[3]))
    if film[5] == "COMEDY":
        COMEDY_RATING_1.append(float(film[1]))
        COMEDY_RATING_3.append(float(film[3]))


g1 = (ACTION_RATING_1, ACTION_RATING_3)
g2 = (ROMANCE_RATING_1, ROMANCE_RATING_3)
g3 = (COMEDY_RATING_1, COMEDY_RATING_3)

data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("ACTION", "ROMANCE", "COMEDY")
markers = (".", "^", "s")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group, mark in zip(data, colors, groups, markers):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group, marker = mark)

plt.title('scatter plot for genres')
plt.xlabel("AVGRATING_WEBSITE_1")
plt.ylabel("AVGRATING_WEBSITE_3")
plt.legend(loc=2)
plt.show()
