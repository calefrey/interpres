from sklearn.ensemble import RandomForestClassifier
import numpy as np
from joblib import dump
data = []
labels = []

for row in np.loadtxt("training-data.txt", dtype=None, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)):
    # sensor data is in all but first column
    data.append(row)

for label in np.loadtxt("training-data.txt", dtype=str, usecols=0):
    #labels are first column
    labels.append(label)


clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(data, labels)

dump(clf, 'classifier.joblib') # saves the trained classifier to file