import random
import pandas as pd

def generate_message(is_scam, language="English", country="Kenya"):
    if language == "English":
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
    elif language == "Swahili":
        if is_scam:
            return random.choice([
                "Mteja mpendwa, akaunti yako ya M-Pesa iko hatarini! Bofya hapa kuthibitisha: http://fake-mpesa.com",
                "Umetumiwa KSh 45,000 kutoka 0721xxxxxx. Thibitisha sasa au itarudishwa!",
                "HARAKA: SIM yako itazuiwa kwa masaa 24. Piga 0112xxxxxx mara moja."
            ])
        else:
            return random.choice([
                "Thibitisho la M-Pesa: Umetuma KSh 500 kwa John. Saa: 14:30",
                "Umetumiwa KSh 1200 kutoka Mama Mboga. Salio jipya KSh 4500"
            ])

country = "Kenya"

data = []

for i in range(15000):
    is_scam = random.random() < 0.05
    lang = random.choice(["English", "Swahili"])
    message = generate_message(is_scam, lang, country)

    data.append({
        "message": message,
        "is_fraud": int(is_scam),
        "language": lang,
        "country": country
    })

df = pd.DataFrame(data)
df.to_csv("data/synthetic_african_fraud_data.csv", index=False)

print("✅ Done! Created 15,000 messages.")
print("Scams:", df["is_fraud"].sum())