import yfinance as yf

Amazon = yf.Ticker("AMZN")

nombres=["AMZN"]
cotizaciones=[]

"""
for i in range(len(nombres)):
    df = yf.download(nombres[0], start="2021-09-03", end="2021-09-04",group_by="ticker")
    open= list(df["Open"])
    close = list(df["Close"])

    if open < close:
        cotizaciones.append(close/open)
    elif open > close:
        cotizaciones.append((close/open)-1)
"""

a=[13]
b=a[0]
df = yf.download(nombres[0], start="2021-09-03", end="2021-09-04",group_by="ticker")
print(b)
"""
if list(df["Open"])<list(df["Close"]):
    print("hola")
elif list(df["Open"])>list(df["Close"]):
    pass
print(list(df["Open"]))
print(list(df["Close"]))
"""
"""
print(Amazon.info['open']) #Precio al que vendo una acción
print(Amazon.info['previousClose']) #Precio al que vendo una acción
print(Amazon.info['regularMarketPreviousClose']) #Precio al que vendo una acción
"""



#3462.520020 close