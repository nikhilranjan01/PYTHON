import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc

# Load dataset and prepare binary classification
data = load_iris()
X = data.data
y = (data.target == 0).astype(int)  # Binary classification: class '0' vs. others

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train classifiers
clf1 = LogisticRegression()
clf1.fit(X_train, y_train)
y_probs1 = clf1.predict_proba(X_test)[:, 1]

clf2 = RandomForestClassifier()
clf2.fit(X_train, y_train)
y_probs2 = clf2.predict_proba(X_test)[:, 1]

# Compute ROC curve and AUC
fpr1, tpr1, _ = roc_curve(y_test, y_probs1)
auc1 = auc(fpr1, tpr1)

fpr2, tpr2, _ = roc_curve(y_test, y_probs2)
auc2 = auc(fpr2, tpr2)

# Plot ROC curves
plt.figure()
plt.plot(fpr1, tpr1, label=f'Logistic Regression (AUC = {auc1:.2f})')
plt.plot(fpr2, tpr2, label=f'Random Forest (AUC = {auc2:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()
