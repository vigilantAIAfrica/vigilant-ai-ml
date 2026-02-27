import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

df = pd.read_csv("data/cleaned_features.csv")
labels = pd.read_csv("data/labels.csv").values.ravel()

X_train, X_test, y_train, y_test = train_test_split(
    df, labels, test_size=0.2, random_state=42
)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

preds = tree.predict(X_test)

print("Decision Tree F1:", f1_score(y_test, preds))

joblib.dump(tree, "models/tree_model.pkl")