import requests
import numpy as np

companySymbol = "SNAP"
token = "lOYxqIv2o28R3BhkYboGZSKAvfrAXaULS5tLXOyWXm6Tg6OmnaHaeBSOtOhC"

# setting up url to retrive stock price information
URL = "https://api.worldtradingdata.com/api/v1/history?symbol=" + companySymbol + "&api_token=" + token

# calling the api
r = requests.get(URL)
# getting the data as json
data = r.json()

#here we are decoding it so we get the close price
history = data["history"]
close = []

for key in history:
    close.append(history[key]["close"])

#converting it to an numpy array as from string to float
npClose = np.array(close).astype(np.float)
# getting the mean value of the close price
mean = np.mean(npClose)

# minutes
interval = "60"

url = "https://intraday.worldtradingdata.com/api/v1/intraday?symbol=" + companySymbol + "&interval=" + interval \
      + "&range=1&api_token=" + token

R = requests.get(url)
Data = R.json()

intraday = Data["intraday"]
latestClose = 0
for key in intraday:
    latestClose = float(intraday[key]["close"])

if latestClose > mean:
    print("you should probably sell your stock because the stock estimated mean is:  " + str(mean) +
          " sooner or later it will drop to the mean value, latest close price is: " + str(latestClose))
elif latestClose < mean:
    print("You should probably buy this stock at the latest close price: " + str(latestClose) +
          " because this price is lower than the mean price which is: " + str(mean))


print("\n THIS CALCULATION IS VERY SIMPLE AND DO NOT TAKE IT FOR GRANTED AS IT COULD BE WRONG, " +
      "BUT IT'S MATHIMATICALLY CORRECT AND MATH DOESN'T LIE...")