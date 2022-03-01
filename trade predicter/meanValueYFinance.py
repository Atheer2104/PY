import yfinance as yf
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
from operator import itemgetter

## getting current date and calculating what the date would be four months back
## a period consist of 4 month
period = str(date.today()-relativedelta(months=+7))

companies = ["NAS.OL", "PAX.ST", "SPEQT.ST", "OSSD.ST"]
## getting stock price info
data = yf.download(companies, start=""+period)

companiesCalculatedInfo = []
for company in companies:
    # calculating mean value
    meanValue = np.mean(data["Close"][company])
    # getting the current stock price
    latestClose = (data["Close"][company][-1]).astype(np.float)
    # calculating the differnce between mean and close if the value will be converted from positve to negativ and vice versa
    # negativ (-) indicates that the company current close is below the mean value
    # positive (+) indicated that the company current close price is above the estimated mean
    differennceMeanMinusClose = -(meanValue-latestClose)
    # adding the mean value and latest close to an array along with the name of the compay
    companiesCalculatedInfo.append(["Symbol:", str(company), "DifferenceMean&Close", differennceMeanMinusClose, "MeanValue:",
                              meanValue, "LatestClose:", latestClose])


#sorting the array based on the DifferenceMean&Close value
sortedCompaniesCalculatedInfo = sorted(companiesCalculatedInfo, key=itemgetter(3))
## printing the sorted array out
for company in sortedCompaniesCalculatedInfo:
    print(company)
    print("\r")
