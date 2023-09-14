import streamlit as st
import yfinance as yf

def normalize(value, min_value, max_value):
    value = max(min(value, max_value), min_value)  # Clamping the value
    return (value - min_value) / (max_value - min_value)

def day_trader_index(ticker):
    # ... [Your day_trader_index function implementation]
    stock = yf.Ticker(ticker)
    history = stock.history(period="5d", interval="1m")
    current_price = history["Close"].iloc[-1]
    moving_average_15m = history["Close"].tail(15).mean()
    moving_average_15m_norm = normalize(moving_average_15m, history["Close"].min(), history["Close"].max())
    volume = history["Volume"].tail(15).mean()
    volume_norm = normalize(volume, history["Volume"].min(), history["Volume"].max())
    support = history["Low"].min()
    resistance = history["High"].max()
    support_resistance_diff = (current_price - support) / (resistance - support)
    volatility = history["High"].sub(history["Low"]).mean()
    volatility_norm = normalize(volatility, 0, current_price * 0.1)
    index = (
        0.35 * moving_average_15m_norm +
        0.30 * volume_norm +
        0.20 * support_resistance_diff +
        0.15 * volatility_norm
    )
    return index * 100

def position_trader_index(ticker):
    # ... [Your position_trader_index function implementation]
    stock = yf.Ticker(ticker)
    history = stock.history(period="2y")
    info = stock.info
    current_price = history["Close"].iloc[-1]
    moving_average_150d = history["Close"].tail(150).mean()
    moving_average_150d_norm = normalize(moving_average_150d, history["Close"].min(), history["Close"].max())
    volume = history["Volume"].tail(20).mean()
    volume_norm = normalize(volume, history["Volume"].min(), history["Volume"].max())
    support = history["Low"].min()
    resistance = history["High"].max()
    support_resistance_diff = (current_price - support) / (resistance - support)
    pe_ratio = info.get("trailingPE", current_price)
    pe_norm = normalize(pe_ratio, 5, 50)
    dividend_yield = info.get("dividendYield", 0)
    dy_norm = normalize(dividend_yield, 0, 0.1)
    debt_to_equity = info.get("debtToEquity", 0)
    debt_norm = normalize(debt_to_equity, 0, 2)
    eps_growth = info.get("earningsQuarterlyGrowth", 0)
    eps_norm = normalize(eps_growth, -1, 1)
    free_cash_flow = info.get("freeCashflow", 0) / info.get("marketCap", 1)
    fcf_norm = normalize(free_cash_flow, 0, 0.2)
    index = (
        0.25 * moving_average_150d_norm +
        0.05 * volume_norm +
        0.05 * support_resistance_diff +
        0.20 * pe_norm +
        0.10 * dy_norm +
        0.10 * debt_norm +
        0.15 * eps_norm +
        0.10 * fcf_norm
    )
    return index * 100

def swing_trader_index(ticker):
    # ... [Your swing_trader_index function implementation]
    stock = yf.Ticker(ticker)
    history = stock.history(period="1y")
    info = stock.info
    current_price = history["Close"].iloc[-1]
    moving_average_50d = history["Close"].tail(50).mean()
    moving_average_50d_norm = normalize(moving_average_50d, history["Close"].min(), history["Close"].max())
    volume = history["Volume"].tail(10).mean()
    volume_norm = normalize(volume, history["Volume"].min(), history["Volume"].max())
    support = history["Low"].min()
    resistance = history["High"].max()
    support_resistance_diff = (current_price - support) / (resistance - support)
    pe_ratio = info.get("trailingPE", current_price)
    pe_norm = normalize(pe_ratio, 5, 50)
    eps_growth = info.get("earningsQuarterlyGrowth", 0)
    eps_norm = normalize(eps_growth, -1, 1)
    index = (
        0.30 * moving_average_50d_norm +
        0.10 * volume_norm +
        0.10 * support_resistance_diff +
        0.25 * pe_norm +
        0.25 * eps_norm
    )
    return index * 100

def buy_and_hold_investor_index(ticker):
    # ... [Your buy_and_hold_investor_index function implementation]
    stock = yf.Ticker(ticker)
    history = stock.history(period="5y")
    info = stock.info
    current_price = history["Close"].iloc[-1]
    moving_average_200d = history["Close"].tail(200).mean()
    moving_average_200d_norm = normalize(moving_average_200d, history["Close"].min(), history["Close"].max())
    volume = history["Volume"].tail(50).mean()
    volume_norm = normalize(volume, history["Volume"].min(), history["Volume"].max())
    pe_ratio = info.get("trailingPE", current_price)
    pe_norm = normalize(pe_ratio, 5, 50)
    dividend_yield = info.get("dividendYield", 0)
    dy_norm = normalize(dividend_yield, 0, 0.1)
    debt_to_equity = info.get("debtToEquity", 0)
    debt_norm = normalize(debt_to_equity, 0, 2)
    roe = info.get("returnOnEquity", 0)
    roe_norm = normalize(roe, 0, 0.3)
    eps_growth_5y = info.get("earningsQuarterlyGrowth", 0)
    eps_growth_5y_norm = normalize(eps_growth_5y, -1, 1)
    free_cash_flow = info.get("freeCashflow", 0) / info.get("marketCap", 1)
    fcf_norm = normalize(free_cash_flow, 0, 0.2)
    index = (
        0.15 * moving_average_200d_norm +
        0.05 * volume_norm +
        0.20 * pe_norm +
        0.20 * dy_norm +
        0.10 * debt_norm +
        0.10 * roe_norm +
        0.15 * eps_growth_5y_norm +
        0.05 * fcf_norm
    )
    return index * 100

def value_investor_index_normalized(ticker):
    # ... [Your value_investor_index_normalized function implementation]
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

index_functions = {
    "Day Trader Index": day_trader_index,
    "Position Trader Index": position_trader_index,
    "Swing Trader Index": swing_trader_index,
    "Buy and Hold Investor Index": buy_and_hold_investor_index,
    "Value Investor Index": value_investor_index_normalized
}

# Streamlit UI
st.title("Stock Index Calculator")

# Input for stock ticker
ticker = st.text_input("Enter the stock ticker:")

# Dropdown for selecting the index
index_choice = st.selectbox(
    "Select the index you want to calculate:",
    list(index_functions.keys())
)

# Button to calculate the index
if st.button("Calculate Index"):
    if ticker:
        index_value = index_functions[index_choice](ticker)
        st.write(f"The {index_choice} for {ticker} is: {index_value:.2f}")
    else:
        st.write("Please enter a stock ticker.")
