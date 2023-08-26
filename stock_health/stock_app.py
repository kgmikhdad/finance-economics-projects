import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# Fetch stock data and info
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")
    info = stock.info
    return data, info

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
def get_recommendation(fundamentals, technicals):
    buy_signals = 0
    sell_signals = 0

    # Fundamental checks
    if fundamentals["P/E"] < 20:
        buy_signals += 1
    else:
        sell_signals += 1

    if fundamentals["P/B"] < 1:
        buy_signals += 1
    else:
        sell_signals += 1

    # Technical checks
    if technicals["Close"] > technicals["MA50"]:
        buy_signals += 1
    else:
        sell_signals += 1

    if technicals["MACD"] > technicals["MACD_signal"]:
        buy_signals += 1
    else:
        sell_signals += 1

    # Final recommendation
    if buy_signals > sell_signals:
        return "Buy"
    elif sell_signals > buy_signals:
        return "Sell"
    else:
        return "Hold"

# Streamlit App
st.title("Stock Health Checker")

ticker = st.text_input("Enter Stock Ticker:", value="AAPL").upper()

if st.button("Check Stock Health"):
    try:
        data, stock_info = get_stock_data(ticker)
        data = compute_technical_indicators(data)
        
        st.subheader("Fundamental Indicators")
        fundamentals = {
            "ROI": stock_info.get("returnOnInvestment", "N/A"),
            "EBITDA": stock_info.get("ebitda", "N/A"),
            "EPS": stock_info.get("trailingEps", "N/A"),
            "P/E": stock_info.get("trailingPE", "N/A"),
            "P/B": stock_info.get("priceToBook", "N/A"),
            # ... [Add other fundamental indicators here] ...
        }
        st.write(fundamentals)
        
        st.subheader("Technical Indicators")
        technicals = {
            "MA50": data["MA50"].iloc[-1],
            "MA200": data["MA200"].iloc[-1],
            "RSI": data["RSI"].iloc[-1],
            "MACD": data["MACD"].iloc[-1],
            "MACD Signal": data["MACD_signal"].iloc[-1],
            # ... [Add other technical indicators here] ...
        }
        st.write(technicals)
        
        recommendation = get_recommendation(fundamentals, technicals)
        st.subheader(f"Recommendation: {recommendation}")
        
    except Exception as e:
        st.write(f"Error: {e}")

