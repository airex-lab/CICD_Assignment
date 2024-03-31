import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC


df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

#model = LogisticRegression().fit(X, y)
#model_decision = DecisionTreeClassifier()
#model = RandomForestClassifier().fit(X, y)
#model = GradientBoostingClassifier().fit(X, y)
model = GaussianNB().fit(X, y)
# model = AdaBoostClassifier(GaussianNB(), n_estimators=50).fit(X, y)
# model = SVC(kernel='poly').fit(X, y)
# model = AdaBoostClassifier(SVC(), n_estimators=50,algorithm='SAMME').fit(X,y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
