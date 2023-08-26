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
    # ... [Same as previous code for technical indicators] ...

# Recommendation based on indicators
def get_recommendation(fundamentals, technicals):
    # Basic logic for recommendation
    # This is a very rudimentary recommendation system. In a real-world scenario, more sophisticated algorithms would be used.
    buy_signals = 0
    sell_signals = 0

    # Fundamental checks
    if fundamentals["P/E"] < 20:  # P/E ratio less than 20 is generally considered good
        buy_signals += 1
    else:
        sell_signals += 1

    if fundamentals["P/B"] < 1:  # P/B ratio less than 1 might indicate the stock is undervalued
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

