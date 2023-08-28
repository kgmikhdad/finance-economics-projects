import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def plot_stock_chart(stock_name):
    # Fetch data
    stock = yf.Ticker(stock_name)
    hist_data = stock.history(period='1y')
    
    # Check if data was fetched successfully
    if hist_data.empty:
        st.write(f"No data available for {stock_name}. Please enter a valid stock ticker.")
        return
    
    # Plotting the stock data
    fig = go.Figure(data=[go.Candlestick(x=hist_data.index,
                                         open=hist_data['Open'],
                                         high=hist_data['High'],
                                         low=hist_data['Low'],
                                         close=hist_data['Close'])])
    
    fig.update_layout(title=f'{stock_name} Stock Price Over the Last Year',
                      xaxis_title='Date',
                      yaxis_title='Stock Price',
                      xaxis_rangeslider_visible=False)
    
    st.plotly_chart(fig)

# Streamlit UI
st.title('Stock Price Chart App')
stock_name = st.text_input('Enter the stock name (e.g. AAPL for Apple): ')

if stock_name:
    plot_stock_chart(stock_name)
