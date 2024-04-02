import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

# Load the dataset
df = pd.read_csv("data/train.csv")

# Features and original labels
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()

# Create a shuffled version of the labels to disrupt the label-feature relationship
np.random.seed(0)  # Ensure reproducibility
shuffled_y = np.random.permutation(y)

# Train the model on the disrupted dataset
model = LogisticRegression(max_iter=1000).fit(X, shuffled_y)

# Save the model
with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
