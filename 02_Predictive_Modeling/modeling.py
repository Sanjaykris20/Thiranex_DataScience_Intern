import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/intern 4th sem/02_Predictive_Modeling/customer_churn_data.csv")

# Split features & labels
X = df.drop(columns=['CustomerID', 'Churn'])
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 1. Train Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
y_prob_lr = lr.predict_proba(X_test)[:, 1]

# 2. Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_prob_rf = rf.predict_proba(X_test)[:, 1]

# Calculate metrics for Logistic Regression
acc_lr = accuracy_score(y_test, y_pred_lr)
prec_lr = precision_score(y_test, y_pred_lr)
rec_lr = recall_score(y_test, y_pred_lr)
f1_lr = f1_score(y_test, y_pred_lr)
cm_lr = confusion_matrix(y_test, y_pred_lr).tolist() # [[TN, FP], [FN, TP]]

# Calculate metrics for Random Forest
acc_rf = accuracy_score(y_test, y_pred_rf)
prec_rf = precision_score(y_test, y_pred_rf)
rec_rf = recall_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)
cm_rf = confusion_matrix(y_test, y_pred_rf).tolist()

# ROC Curve for RF
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)

# ROC Curve for LR
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
roc_auc_lr = auc(fpr_lr, tpr_lr)

# Feature Importances for RF
importances = rf.feature_importances_
feature_names = X.columns
feat_imp = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
feat_imp_dict = {name: float(imp) for name, imp in feat_imp}

# Get Logistic Regression Coefficients for interactive JS prediction
coefs = lr.coef_[0]
intercept = lr.intercept_[0]
lr_coefficients = {
    "intercept": float(intercept),
    "features": {name: float(coef) for name, coef in zip(X.columns, coefs)}
}

# Save metadata for UI
model_data = {
    "lr_metrics": {
        "accuracy": float(acc_lr),
        "precision": float(prec_lr),
        "recall": float(rec_lr),
        "f1": float(f1_lr),
        "cm": cm_lr,
        "auc": float(roc_auc_lr)
    },
    "rf_metrics": {
        "accuracy": float(acc_rf),
        "precision": float(prec_rf),
        "recall": float(rec_rf),
        "f1": float(f1_rf),
        "cm": cm_rf,
        "auc": float(roc_auc_rf)
    },
    "roc_curve_rf": {
        "fpr": fpr_rf.tolist(),
        "tpr": tpr_rf.tolist()
    },
    "roc_curve_lr": {
        "fpr": fpr_lr.tolist(),
        "tpr": tpr_lr.tolist()
    },
    "feature_importances": feat_imp_dict,
    "lr_formula": lr_coefficients
}

with open("C:/Users/HP/Downloads/intern 4th sem/02_Predictive_Modeling/model_data.js", "w") as f:
    f.write(f"const modelResults = {json.dumps(model_data)};\n")

print("ML Modeling complete! model_data.js created with model parameters.")
print(f"Random Forest Accuracy: {acc_rf:.4f}, LR Accuracy: {acc_lr:.4f}")
