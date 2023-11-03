import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock Price Analysis")

st.write("""
         Shown are the stock closing price and volume of Google (GOOGL)
         """)

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

start_date = st.date_input("Start Date", pd.to_datetime('2010-05-31'))
end_date = st.date_input("End Date", pd.to_datetime('2023-11-01'))

tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

st.write("## Closing Price")
st.line_chart(tickerDf['Close'])

st.write("## Volume")
st.line_chart(tickerDf['Volume'])

