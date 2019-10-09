import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import sklearn
import graphviz
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

col_names = ['FILM_ID','AVGRATING_WEBSITE_1','AVGRATING_WEBSITE_2','AVGRATING_WEBSITE_3','AVGRATING_WEBSITE_4','GENRE']
# load dataset
pima = pd.read_csv("data-film.csv", encoding='utf-8', header=None, names=col_names)[1:]
pima.head()

feature_cols = ['AVGRATING_WEBSITE_1', 'AVGRATING_WEBSITE_2', 'AVGRATING_WEBSITE_3']
X = pima[feature_cols] # Features
y = pima.GENRE # Target variable

clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X, y)

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['ACTION','ROMANCE','COMEDY'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('data-film.png')
Image(graph.create_png())
