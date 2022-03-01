import requests
import numpy as np

companySymbol = "SNAP"
apiToken = "QCK0LZS4H34T2JQN"

## we are going the take the history for the past 5 years only not more 
URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + companySymbol + "&outputsize=full&apikey=" + apiToken

r = requests.get(URL)
data = r.json()

history = data["Time Series (Daily)"]
close = []

for date in history:
    close.append(history[date]["4. close"])

#converting it to an numpy array as from string to float
npClose = np.array(close).astype(np.float)
# getting the mean value of the close price
mean = np.mean(npClose)

print(mean)