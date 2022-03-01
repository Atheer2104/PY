import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

#getting the file
df = pd.read_csv('breast-cancer-wisconsin.data.txt')

#replacing missing data 
df.replace('?', -99999, inplace=True)

#droping id useless data
df.drop(['id'],1, inplace=True)

#features
X = np.array(df.drop(['class'],1))

#label
y = np.array(df['class'])

#shuffling the train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

#setting up clf
#clf = neighbors.KNeighborsClassifier()

#fitting x and y
#lf.fit(X_train, y_train)

#with open('breastcancer.pickle', 'wb') as f:
#    pickle.dump(clf, f)

pickle_in = open('breastcancer.pickle', 'rb')
clf = pickle.load(pickle_in)



#getting the accuracy 
accuracy = clf.score(X_test,y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,2 ,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)

prediction = clf.predict(example_measures)
print(prediction)
