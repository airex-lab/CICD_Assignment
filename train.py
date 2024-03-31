import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

#model = LogisticRegression()
#model = RandomForestClassifier(n_estimators=100, random_state=42)
model = SVC(kernel='linear', random_state=42)
model.fit(X, y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
