import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

def get_data(stock):
    # ... [same as before]

def plot_stock_chart(stock):
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="1y")

    # Plotting the stock's closing prices
    plt.figure(figsize=(10, 6))
    hist['Close'].plot(title=f'{stock} Stock Price Over the Last Year')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    st.pyplot(plt)

def main():
    st.title("Stock Fundamental and Technical Indicators")

    stock = st.text_input("Enter stock ticker (e.g. AAPL):")

    if stock:
        fundamentals, technicals = get_data(stock)

        st.write("## Fundamental Indicators")
        st.write(fundamentals)

        st.write("## Technical Indicators")
        st.write(technicals)

        st.write("## Stock Price Chart")
        plot_stock_chart(stock)

if __name__ == "__main__":
    main()
 
