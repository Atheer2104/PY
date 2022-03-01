import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

#choosing what graf style to use
style.use('ggplot')


#getting data
df = quandl.get('WIKI/GOOGL')

#getting data we need
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

#getting percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

#the new divided by the old 'andel'
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

#sorting out data to only use the useful ones
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

# the data we are going to predict
forecast_col = 'Adj. Close'

# filling this data with anything we don't want to get rid of it
df.fillna(-99999, inplace=True)

#math.ceil returning whole numbers and predcting what price it will -
#- have the next 10 days '0.01'
forecast_out = int(math.ceil(0.1*len(df)))
print(forecast_out)

#assign values and shifting colums
df['label'] = df[forecast_col].shift(-forecast_out)

#getting everything expect label column
X = np.array(df.drop(['label', 'Adj. Close'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

#scaling the new values from the old

df.dropna(inplace=True)
y = np.array(df['label'])

#training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#n-jobs how many times do we want run with our processor 
#clf = LinearRegression(n_jobs=-1)
#clf.fit(X_train, y_train)
#with open('linearregression.pickle', 'wb') as f:
#    pickle.dump(clf, f)

pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

#we are training data because it will be the same answear because they havealready seen them
accuracy = clf.score(X_test, y_test)

#here we are predicting 
forecast_Set = clf.predict(X_lately)

print(forecast_Set, accuracy, forecast_out)

df['Forecast'] = np.nan

#getting the day so we whow what we predict in a day
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_Set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    #setting the above to not number so we can you use in graph
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()







