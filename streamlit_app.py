# import streamlit as st
# import FinanceDataReader as fdr

# code = st.text_input("종목 코드를 입력해주세요")
# data = fdr.DataReader(code)
# st.write(data)

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import date, timedelta
import time

st.title('Real-time Stock Price Visualization')

# Get user input
ticker = st.text_input("Enter a ticker symbol (e.g. TSLA): ", 'TSLA')
start_date = st.date_input("Start date", date.today() - timedelta(days=365))
end_date = st.date_input("End date", date.today())

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Initialize the figure
fig = go.Figure()

# Create the chart and store it in a variable
chart = st.empty()

for t in range(len(data)):
    # Add the current day's closing price to the chart
    fig.add_trace(go.Scatter(x=data.index[:t+1], y=data['Close'][:t+1], mode='lines'))

    # Display the figure
    chart.plotly_chart(fig)

    # Wait for 1 second before adding the next day
    time.sleep(0.1)

    # Clear the figure for the next day
    fig = go.Figure()

st.write(data)
