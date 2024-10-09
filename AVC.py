import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from sklearn.preprocessing import label_binarize
from sklearn.metrics import RocCurveDisplay

# Load the Wine dataset
data = load_wine()
X, y = data.data, data.target

# Binarize the output labels for multiclass ROC-AUC scoring
y_bin = label_binarize(y, classes=[0, 1, 2])

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
y_bin_train, y_bin_test = train_test_split(y_bin, test_size=0.3, random_state=42)

# Define different Dummy Classifier strategies
strategies = ['constant', 'uniform', 'stratified', 'prior', 'most_frequent']

accuracy_dict = {}
roc_auc_dict = {}
classifiers = {}

# Loop through strategies and fit Dummy Classifier
for strategy in strategies:
    if strategy == 'constant':
        dummy_clf = DummyClassifier(strategy=strategy, constant=0)  # Choosing class 0 as the constant
    else:
        dummy_clf = DummyClassifier(strategy=strategy)
    
    dummy_clf.fit(X_train, y_train)
    y_pred = dummy_clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_dict[strategy] = accuracy

    # Calculate AUC if the classifier can predict probabilities
    if hasattr(dummy_clf, "predict_proba"):
        y_score = dummy_clf.predict_proba(X_test)
        auc = roc_auc_score(y_bin_test, y_score, multi_class='ovr')
        roc_auc_dict[strategy] = auc

    classifiers[strategy] = dummy_clf

# Print results
print("Accuracy of baseline classifiers:")
for strategy, accuracy in accuracy_dict.items():
    print(f"{strategy}: {accuracy:.2f}")

print("\nAUC of baseline classifiers:")
for strategy, auc in roc_auc_dict.items():
    print(f"{strategy}: {auc:.2f}")

# Plot ROC Curves
plt.figure(figsize=(10, 8))
for strategy, dummy_clf in classifiers.items():
    if hasattr(dummy_clf, "predict_proba"):
        y_score = dummy_clf.predict_proba(X_test)
        for i in range(y_bin_test.shape[1]):
            fpr, tpr, _ = roc_curve(y_bin_test[:, i], y_score[:, i])
            RocCurveDisplay(fpr=fpr, tpr=tpr).plot(ax=plt.gca(), name=f"{strategy} (class {i})")
            
plt.title('ROC Curves for Baseline Classifiers')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()
