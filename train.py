import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
#labels = np.sort(np.unique(y))
labels = np.array(['Anemia', 'Diabetes', 'Healthy', 'Heart Di', 'Thalasse', 'Thromboc'])
y = np.array([np.where(labels == x) for x in y]).flatten()

#model = LogisticRegression(C=0.01, max_iter=1000).fit(X, y)
model = GradientBoostingClassifier(max_depth = 3, n_estimators = 500, learning_rate = 0.05).fit(X,y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
