from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors

clf1 = svm.SVC()

clf2 = GaussianNB()

clf3 = neighbors.KNeighborsClassifier()

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# Support vector classifier
clf1 = clf1.fit(X,Y)
# Naive Bayes
clf2 = clf2.fit(X,Y)
# K Neighbors Classifier
clf3 = clf3.fit(X,Y)

X_test=[[198,92,48],[184,84,44],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
Y_test=['male','male','male','female','female','female','male','male']

Y_prediction1 = clf1.predict(X_test)
Y_prediction2 = clf2.predict(X_test)
Y_prediction3 = clf3.predict(X_test)

print("Prediction for SVM : ", Y_prediction1)
print("Prediction for Naive bayes : ", Y_prediction2)
print("Prediction for K Neighbors : ", Y_prediction3)

print("Accuracy score for Naive Bayes : ",accuracy_score(Y_test,Y_prediction2))
print("Accuracy score for SVM : ",accuracy_score(Y_test,Y_prediction1))
print("Accuracy score for K Neighbors : ",accuracy_score(Y_test,Y_prediction3))