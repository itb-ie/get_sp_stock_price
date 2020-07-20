import pandas
import yfinance as yf

df_companies = pandas.read_csv("constituents_csv.csv")
companies = df_companies["Symbol"]
#print(companies)

first_time = True

for comp in companies:
    #define the ticker symbol
    tickerSymbol = comp
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(interval='1wk', start='2019-7-1', end='2020-7-1')

    df = pandas.DataFrame()
    #print(tickerDf.head(2))
    #print(tickerDf.columns.values)
    #print(tickerDf[tickerDf["Close"] > 0]["Close"])
    #print(tickerDf[tickerDf["Close"] > 0]["Close"].size)
    df["Close Value"] = tickerDf[tickerDf["Close"] > 0]["Close"].copy()
    df["Ticker"] = comp
    print(df)
    if first_time:
        df.to_csv("results.csv")
    else:
        df.to_csv("results.csv", mode="a", header=False)
    first_time = False


'''
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(interval='1wk', start='2019-7-1', end='2020-7-1')

df = pandas.DataFrame()
#print(tickerDf.head(2))
#print(tickerDf.columns.values)
print(tickerDf[tickerDf["Close"] > 0]["Close"])
print(tickerDf[tickerDf["Close"] > 0]["Close"].size)
df["Close Value"] = tickerDf[tickerDf["Close"] > 0]["Close"].copy()
df["Ticker"] = "AAPL"
print(df)
df.to_csv("results.csv", mode="a", header=False)
'''