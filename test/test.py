import streamlit as st
import yfinance as yf

def normalize(value, min_value, max_value):
    value = max(min(value, max_value), min_value)  # Clamping the value
    return (value - min_value) / (max_value - min_value)

def value_investor_index(ticker):
    stock = yf.Ticker(ticker)
    history = stock.history(period="5y")
    info = stock.info
    current_price = history["Close"].iloc[-1]
    moving_average = history["Close"].tail(50).mean()
    moving_average_norm = normalize(moving_average, history["Close"].min(), history["Close"].max())
    volume = history["Volume"].tail(50).mean()
    volume_norm = normalize(volume, history["Volume"].min(), history["Volume"].max())
    support = history["Low"].min()
    resistance = history["High"].max()
    support_resistance_diff = (current_price - support) / (resistance - support)
    pe_ratio = info.get("trailingPE", current_price)
    pe_norm = normalize(pe_ratio, 5, 50)
    pb_ratio = info.get("priceToBook", 1)
    pb_norm = normalize(pb_ratio, 0, 10)
    dividend_yield = info.get("dividendYield", 0)
    dy_norm = normalize(dividend_yield, 0, 0.1)
    debt_to_equity = info.get("debtToEquity", 0)
    debt_norm = normalize(debt_to_equity, 0, 2)
    roe = info.get("returnOnEquity", 0)
    roe_norm = normalize(roe, 0, 0.3)
    eps_growth = info.get("earningsQuarterlyGrowth", 0)
    eps_norm = normalize(eps_growth, -1, 1)
    free_cash_flow = info.get("freeCashflow", 0) / info.get("marketCap", 1)
    fcf_norm = normalize(free_cash_flow, 0, 0.2)
    book_value = info.get("bookValue", 1)
    bv_norm = normalize(book_value, 0, 100)
    current_ratio = info.get("currentRatio", 1)
    cr_norm = normalize(current_ratio, 0, 5)
    index = (
        0.04 * moving_average_norm +
        0.02 * volume_norm +
        0.01 * support_resistance_diff +
        0.20 * pe_norm +
        0.15 * pb_norm +
        0.15 * dy_norm +
        0.12 * debt_norm +
        0.12 * roe_norm +
        0.10 * eps_norm +
        0.08 * fcf_norm +
        0.05 * bv_norm +
        0.05 * cr_norm
    )
    return index * 100
# Streamlit UI
st.title("Value Investor Index Calculator")

# Input for stock ticker
ticker = st.text_input("Enter the stock ticker:")

# Button to calculate the index
if st.button("Calculate Index"):
    if ticker:
        index_value = value_investor_index(ticker)
        st.write(f"The Value Investor Index for {ticker} is: {index_value:.2f}")
    else:
        st.write("Please enter a stock ticker.")
