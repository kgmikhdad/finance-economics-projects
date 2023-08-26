import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# Fetch stock data
def get_stock_data(ticker):
    data = yf.Ticker(ticker)
    return data.history(period="1y")

# Compute technical indicators
def compute_technical_indicators(data):
    # Moving Averages
    data['MA50'] = data['Close'].rolling(50).mean()
    data['MA200'] = data['Close'].rolling(200).mean()
    
    # RSI
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    data['MACD'] = data['Close'].ewm(span=12, adjust=False).mean() - data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD_signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # Bollinger Bands
    data['BB_upper'] = data['Close'].rolling(20).mean() + 2*data['Close'].rolling(20).std()
    data['BB_lower'] = data['Close'].rolling(20).mean() - 2*data['Close'].rolling(20).std()
    
    # Stochastic Oscillator
    high14 = data['High'].rolling(14).max()
    low14 = data['Low'].rolling(14).min()
    data['%K'] = (data['Close'] - low14) / (high14 - low14) * 100
    data['%D'] = data['%K'].rolling(3).mean()
    
    return data

# Recommendation based on indicators
def get_recommendation(data):
    # Basic logic for recommendation
    if data['Close'].iloc[-1] > data['MA50'].iloc[-1] and data['MACD'].iloc[-1] > data['MACD_signal'].iloc[-1]:
        return "Buy"
    elif data['Close'].iloc[-1] < data['MA50'].iloc[-1] and data['MACD'].iloc[-1] < data['MACD_signal'].iloc[-1]:
        return "Sell"
    else:
        return "Hold"

# Streamlit App
st.title("Stock Recommendation App")

ticker = st.text_input("Enter Stock Ticker:", value="AAPL").upper()

if st.button("Get Recommendation"):
    try:
        data = get_stock_data(ticker)
        data = compute_technical_indicators(data)
        
        st.subheader("Fundamental Indicators")
        fundamentals = {
            "Open": data["Open"].iloc[-1],
            "High": data["High"].iloc[-1],
            "Low": data["Low"].iloc[-1],
            "Close": data["Close"].iloc[-1],
            "Volume": data["Volume"].iloc[-1],
            "Dividends": data["Dividends"].iloc[-1],
            "Stock Splits": data["Stock Splits"].iloc[-1],
            "52 Week High": data["High"].max(),
            "52 Week Low": data["Low"].min(),
            "Market Cap": yf.Ticker(ticker).info["marketCap"]
        }
        st.write(fundamentals)
        
        st.subheader("Technical Indicators")
        technicals = {
            "MA50": data["MA50"].iloc[-1],
            "MA200": data["MA200"].iloc[-1],
            "RSI": data["RSI"].iloc[-1],
            "MACD": data["MACD"].iloc[-1],
            "MACD Signal": data["MACD_signal"].iloc[-1],
            "Bollinger Upper": data["BB_upper"].iloc[-1],
            "Bollinger Lower": data["BB_lower"].iloc[-1],
            "Stochastic %K": data["%K"].iloc[-1],
            "Stochastic %D": data["%D"].iloc[-1]
        }
        st.write(technicals)
        
        recommendation = get_recommendation(data)
        st.subheader(f"Recommendation: {recommendation}")
        
    except Exception as e:
        st.write(f"Error: {e}")

