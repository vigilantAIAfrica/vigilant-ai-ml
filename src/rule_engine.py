import re
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

def rule_based_score(message):
    if re.search("fake|urgent|click|call", message.lower()):
        return 1
    return 0

df = pd.read_csv("data/cleaned_features.csv")
labels = pd.read_csv("data/labels.csv").values.ravel()

X_train, X_test, y_train, y_test = train_test_split(
    df, labels, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Logistic Regression F1:", f1_score(y_test, preds))

joblib.dump(model, "models/logistic_model.pkl")