import streamlit as st
import yfinance as yf
import ta
import plotly.graph_objects as go

def display_stock_indicators(stock_name):
    stock = yf.Ticker(stock_name)
    hist_data = stock.history(period='1y')
    
    if hist_data.empty:
        st.write(f"No data available for {stock_name}. Please enter a valid stock ticker.")
        return
    
    # Fundamental Indicators
    stock_info = stock.info
    fundamental_data = {
        'Earnings Per Share (EPS)': stock_info.get('trailingEps', 'N/A'),
        'Price-to-Earnings Ratio (P/E)': stock_info.get('trailingPE', 'N/A'),
        'Price-to-Book Ratio (P/B)': stock_info.get('priceToBook', 'N/A'),
        'Dividend Yield': stock_info.get('dividendYield', 'N/A')
    }
    
    st.subheader(f'Fundamental Indicators for {stock_name}')
    for indicator, value in fundamental_data.items():
        st.write(f'{indicator}: {value}')
    
    # Technical Indicators
    hist_data['MA50'] = hist_data['Close'].rolling(window=50).mean()
    hist_data['EMA50'] = hist_data['Close'].ewm(span=50, adjust=False).mean()
    
    st.subheader(f'Technical Indicators for {stock_name}')
    st.write(f'Moving Average (MA): {hist_data["MA50"].iloc[-1]}')
    st.write(f'Exponential Moving Average (EMA): {hist_data["EMA50"].iloc[-1]}')

    # Interactive Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['MA50'], mode='lines', name='MA50'))
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['EMA50'], mode='lines', name='EMA50'))
    st.plotly_chart(fig)

st.title('Stock Indicators App')
stock_name = st.text_input('Enter the stock name (e.g. AAPL for Apple): ')

if stock_name:
    display_stock_indicators(stock_name)
