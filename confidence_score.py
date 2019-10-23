'''Calculating prediction score of model'''

#Code for model creation before this part
#Model is CLASSIFIER

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import cross_val_score

#Making Confusion Matrix
CM = confusion_matrix(y_val, y_pred)
print("Confusion Matrix")
print(CM)

#Computing subset accuracy
ACCURACY = accuracy_score(y_val, y_pred)
print(ACCURACY)

#print(accuracy_score(y_val, y_pred, normalize = False))
ACCURACIES = cross_val_score(estimator = CLASSIFIER, X = X_train, y = y_train, cv = 10)
print(ACCURACIES.mean())
print(ACCURACIES.std())

#print(CLASSIFIER.score(y))
PROB = CLASSIFIER.predict_proba(X_val)[:, 1]
print(PROB)
print('I am', ACCURACY*100, '%', 'sure that the email is', PROB)
