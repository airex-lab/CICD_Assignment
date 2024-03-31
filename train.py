import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

get_test_success = 1

if get_test_success == 1:
    # To get a model that has an accuracy of > 0.5
    model = GaussianNB().fit(X, y)
else:
    model = LogisticRegression().fit(X, y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
