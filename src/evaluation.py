from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix

# Dummy baseline (Always predict safe)
y_true = [1]*25 + [0]*475  # 5% fraud simulation
y_pred_baseline = [0]*500

print("Baseline F1:", f1_score(y_true, y_pred_baseline))


def evaluate_model(y_true, y_pred):
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1:", f1_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))