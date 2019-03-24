import sensors
from joblib import load
clf = load('classifier.joblib') # loads the trained classifier from file

data = sensors.read()
prediction = clf.predict([data])[0] # returns an array of predictions, so we get the first (and only) value with [0]
print(prediction)