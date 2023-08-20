import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def plot_stock_data(stock_name, duration):
    # Current date
    today = datetime.today().strftime('%Y-%m-%d')
    
    # Calculate start date based on duration
    if duration == '1d':
        start_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    elif duration == '1w':
        start_date = (datetime.today() - timedelta(weeks=1)).strftime('%Y-%m-%d')
    elif duration == '1m':
        start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    elif duration == '3m':
        start_date = (datetime.today() - timedelta(days=90)).strftime('%Y-%m-%d')
    elif duration == '1y':
        start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    else:
        start_date = "2020-01-01"  # Default start date
    
    # Fetch data for the stock
    df = yf.download(stock_name, start=start_date, end=today)

    # Create an interactive line plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name=f'Closing Price of {stock_name}'))

    # Add interactivity and adjustability
    fig.update_layout(
        title=f'Price Plot for {stock_name}',
        xaxis_title='Date',
        yaxis_title='Price',
        hovermode='x'
    )

    # Display the interactive graph
    st.plotly_chart(fig)

def main():
    st.title("Stock Price Plot")
    stock_name = st.text_input("Enter the stock code:", value="AAPL").strip().upper()
    duration = st.selectbox("Choose the duration:", ['1d', '1w', '1m', '3m', '1y'])
    
    if st.button("Plot"):
        plot_stock_data(stock_name, duration)

if __name__ == "__main__":
    main()
