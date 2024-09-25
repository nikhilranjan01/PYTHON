
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn import metrics, model_selection
from sklearn.model_selection import GridSearchCV

cancer = load_breast_cancer(as_frame=True)
df = cancer.frame
X = df.iloc[:, :-1].values 
y = df['target'].values
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2019)

kfold = model_selection.StratifiedKFold(n_splits=5)
clf_DT = DecisionTreeClassifier(random_state=2019).fit(X_train, y_train)
results_DT = model_selection.cross_val_score(clf_DT, X_train, y_train, cv=kfold)
train_acc_DT = results_DT.mean()
test_acc_DT = metrics.accuracy_score(clf_DT.predict(X_test), y_test)

print("Decision Tree (stand alone) - Train:", train_acc_DT)
print("Decision Tree (stand alone) - Test:", test_acc_DT)

num_trees = 100
clf_DT_Bag = BaggingClassifier(estimator=clf_DT, n_estimators=num_trees, random_state=2019).fit(X_train, y_train)
results_DT_Bag = model_selection.cross_val_score(clf_DT_Bag, X_train, y_train, cv=kfold)
train_acc_DT_Bag = results_DT_Bag.mean()
test_acc_DT_Bag = metrics.accuracy_score(clf_DT_Bag.predict(X_test), y_test)

print("\nDecision Tree (Bagging) - Train:", train_acc_DT_Bag)
print("Decision Tree (Bagging) - Test:", test_acc_DT_Bag)
param_grid = {
    'n_estimators': [50, 100, 200],          
    'max_samples': [0.8, 1.0],                    
    'max_features': [0.8, 1.0],                
    'estimator__max_depth': [5, 10, None],       
    'estimator__min_samples_split': [2, 5, 10],    
    'estimator__min_samples_leaf': [1, 2, 4],     
}
clf_DT = DecisionTreeClassifier(random_state=2019)
clf_DT_Bag = BaggingClassifier(estimator=clf_DT, random_state=2019)
grid_search = GridSearchCV(estimator=clf_DT_Bag, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
print("Best parameters found: ", grid_search.best_params_)
print("Best training accuracy: ", grid_search.best_score_)
best_clf = grid_search.best_estimator_
test_accuracy = best_clf.score(X_test, y_test)
print("Test accuracy with best parameters: ", test_accuracy)
