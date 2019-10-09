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


for i in range(0,len(features)):
    for j in range(0,len(features)):
        if i < j:


            X1 = data[features[i]]
            X2 = data[features[j]]

            # X1 = np.array([26604, 49580, 43000, 29500, 31059])
            # X2 = np.array([97000, 94100, 92200, 86500, 79600])
            X1X2 = X1*X2; EX1X2 = np.mean(X1X2)
            # print ('X1X2:',X1X2,'E[X1X2]:',EX1X2)
            mu1 = np.mean(X1); sigma1sq = np.var(X1); sigma1 = np.sqrt(sigma1sq); _sigma1 = np.std(X1)
            mu2 = np.mean(X2); sigma2sq = np.var(X2); sigma2 = np.sqrt(sigma2sq); _sigma2 = np.std(X2)
            # print ('mu1:',mu1,'sigma1sq:',sigma1sq,'sigma1:',sigma1,'_sigma1:',_sigma1)
            # print ('mu2:',mu2,'sigma2sq:',sigma2sq,'sigma2:',sigma2,'_sigma2:',_sigma2)
            sigma12 = EX1X2-mu1*mu2
            rou12 = sigma12/sigma1/sigma2
            # print ('sigma12:',sigma12,'rou12:',rou12)
            corrcoef12 = np.corrcoef(X1, X2)
            _rou12 = corrcoef12[0,1]
            print ('corrcoef',i+1,j+1,':')
            print (corrcoef12)
            print ('_rou',i+1,j+1,':',_rou12)
