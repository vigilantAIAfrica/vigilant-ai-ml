import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
import joblib

def clean_text(text):
    text = text.lower().replace("!", "").replace("?", "").replace("http://", "")
    return text

df = pd.read_csv("data/synthetic_african_fraud_data.csv")
df["cleaned_message"] = df["message"].apply(clean_text)

vectorizer = TfidfVectorizer(max_features=100)
features = vectorizer.fit_transform(df["cleaned_message"])

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(features, df["is_fraud"])

pd.DataFrame(X_resampled.toarray()).to_csv("data/cleaned_features.csv", index=False)
pd.Series(y_resampled).to_csv("data/labels.csv", index=False)

joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Pipeline done! Cleaned and resampled.")