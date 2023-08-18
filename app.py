import streamlit as st
import yfinance as yf
import pandas as pd

def get_data(stock):
    # ... [Keep the existing get_data function as is]

def main():
    st.title("Stock Fundamental and Technical Indicators Dashboard")

    # Sidebar for user input
    st.sidebar.header("Input Stock Ticker")
    stock = st.sidebar.text_input("Enter stock ticker (e.g. AAPL):")

    if stock:
        fundamentals, technicals = get_data(stock)

        # Display stock name and logo
        ticker = yf.Ticker(stock)
        st.image(ticker.info['logo_url'], width=100)
        st.write(f"## {ticker.info['longName']}")

        # Display Fundamental Indicators
        st.write("### Fundamental Indicators")
        fundamentals_df = pd.DataFrame.from_dict(fundamentals, orient='index', columns=['Value'])
        st.table(fundamentals_df)

        # Display Technical Indicators
        st.write("### Technical Indicators")
        technicals_df = pd.DataFrame.from_dict(technicals, orient='index', columns=['Value'])
        st.table(technicals_df)

        # Display stock price chart
        st.write("### Stock Price Chart")
        hist = yf.Ticker(stock).history(period="1y")
        st.line_chart(hist['Close'])

if __name__ == "__main__":
    main()
