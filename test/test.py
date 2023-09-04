import streamlit as st
import yfinance as yf
import ta
import plotly.graph_objects as go
import finviz
from datetime import datetime

def fetch_news(stock_name):
    try:
        news_tables = finviz.get_news(stock_name)
        news = [{'title': item[1], 'url': item[2]} for item in news_tables]
        return news
    except Exception as e:
        st.write(f"Error fetching news: {e}")
        return []

def display_stock_indicators(stock_name, start_date, end_date):
    stock = yf.Ticker(stock_name)
    hist_data = stock.history(start=start_date, end=end_date)
    
    if hist_data.empty:
        st.write(f"No data available for {stock_name}. Please enter a valid stock ticker.")
        return
    
    stock_info = stock.info
    fundamental_data = {
        'Earnings Per Share (EPS)': stock_info.get('trailingEps', 'N/A'),
        'Price-to-Earnings Ratio (P/E)': stock_info.get('trailingPE', 'N/A'),
        'Price-to-Book Ratio (P/B)': stock_info.get('priceToBook', 'N/A'),
        'Dividend Yield': stock_info.get('dividendYield', 'N/A'),
        'Debt-to-Equity Ratio': stock_info.get('debtToEquity', 'N/A'),
        'Return on Equity (ROE)': stock_info.get('returnOnEquity', 'N/A'),
        'Revenue and Revenue Growth': stock_info.get('revenueGrowth', 'N/A'),
        'Net Profit Margin': stock_info.get('profitMargins', 'N/A'),
        'Free Cash Flow': stock_info.get('freeCashflow', 'N/A')
    }
    
    st.subheader(f'Fundamental Indicators for {stock_name}')
    for indicator, value in fundamental_data.items():
        st.write(f'{indicator}: {value}')
    
    # Technical Indicators (same as your original code)
    # ...

    # Feature 1: Interactive Plots
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['MA50'], mode='lines', name='MA50'))
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['EMA50'], mode='lines', name='EMA50'))
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Bollinger High'], mode='lines', name='Bollinger High'))
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Bollinger Low'], mode='lines', name='Bollinger Low'))
    st.plotly_chart(fig)

    # Feature 2: Historical Data Display
    st.subheader(f'Historical Data for {stock_name} from {start_date} to {end_date}')
    st.write(hist_data[['Open', 'High', 'Low', 'Close', 'Volume']])

    # Feature 4: News Feed
    st.subheader(f'Latest News for {stock_name}')
    news = fetch_news(stock_name)
    for article in news:
        st.write(f"**{article['title']}**")
        st.write(f"[Read more]({article['url']})")
        st.write("---")

    # Feature 6: Sentiment Analysis (Placeholder, you can integrate a real sentiment analysis model)
    st.subheader(f'Sentiment Analysis for {stock_name}')
    st.write("Positive sentiment: 60%")
    st.write("Neutral sentiment: 30%")
    st.write("Negative sentiment: 10%")

st.title('Stock Indicators App')
stock_name = st.text_input('Enter the stock name (e.g. AAPL for Apple): ')
start_date = st.date_input("Start date", datetime.now().date().replace(year=datetime.now().year-1))
end_date = st.date_input("End date", datetime.now().date())

if stock_name:
    display_stock_indicators(stock_name, start_date, end_date)
