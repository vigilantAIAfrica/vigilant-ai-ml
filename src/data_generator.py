import random
import pandas as pd
from datetime import datetime

# This makes the messages look real for Kenya
def generate_message(is_scam):
    if is_scam:
        return random.choice([
            "Dear customer, your M-Pesa account is at risk! Click here to verify: http://fake-mpesa.com",
            "You have received KSh 45,000 from 0721xxxxxx. Confirm now or it will be reversed!",
            "URGENT: Your SIM will be blocked in 24hrs. Call 0112xxxxxx immediately."
        ])
    else:
        return random.choice([
            "M-Pesa confirmation: You sent KSh 500 to John. Time: 14:30",
            "You have received KSh 1200 from Mama Mboga. New balance KSh 4500"
        ])

# Create 500 messages (we will make more later)
data = []
for i in range(500):
    is_scam = random.random() < 0.05          # 5% scam messages
    message = generate_message(is_scam)
    data.append({
        "message": message,
        "is_fraud": is_scam,
        "language": "English",
        "country": "Kenya"
    })

# Save to file
df = pd.DataFrame(data)
df.to_csv("data/synthetic_scam_data.csv", index=False)

print("✅ Done! Created 500 realistic messages.")
print("Scam messages:", df["is_fraud"].sum())
print(df.head())