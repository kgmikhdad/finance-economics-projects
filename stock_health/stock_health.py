import streamlit as st
import yfinance as yf
from ta import add_all_ta_features

# Function to fetch stock data
def get_stock_data(ticker):
    data = yf.Ticker(ticker)
    return data.history(period="1y")

# Function to get fundamental indicators
def get_fundamental_indicators(data):
    # For simplicity, we'll fetch some basic indicators. You can expand this list.
    indicators = {
        "Open": data["Open"].iloc[-1],
        "High": data["High"].iloc[-1],
        "Low": data["Low"].iloc[-1],
        "Close": data["Close"].iloc[-1],
        "Volume": data["Volume"].iloc[-1],
        "Dividends": data["Dividends"].iloc[-1],
        "Stock Splits": data["Stock Splits"].iloc[-1],
        # Add more fundamental indicators here
    }
    return indicators

# Function to get technical indicators
def get_technical_indicators(data):
    data = add_all_ta_features(data, open="Open", high="High", low="Low", close="Close", volume="Volume")
    # For simplicity, we'll fetch some basic technical indicators. You can expand this list.
    indicators = {
        "RSI": data["momentum_rsi"].iloc[-1],
        "MACD": data["trend_macd"].iloc[-1],
        "MACD Signal": data["trend_macd_signal"].iloc[-1],
        # Add more technical indicators here
    }
    return indicators

# Streamlit App
st.title("Stock Indicators App")

ticker = st.text_input("Enter Stock Ticker:", value="AAPL").upper()

if st.button("Get Indicators"):
    try:
        data = get_stock_data(ticker)
        st.subheader("Fundamental Indicators")
        st.write(get_fundamental_indicators(data))
        st.subheader("Technical Indicators")
        st.write(get_technical_indicators(data))
    except:
        st.write("Error fetching data. Please check the stock ticker and try again.")

