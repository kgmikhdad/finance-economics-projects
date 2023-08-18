# app.py
import streamlit as st
import yfinance as yf

def get_data(stock):
    ticker = yf.Ticker(stock)
    
    # Fundamental Indicators with error handling for missing keys
    fundamentals = {
        'Market Cap': ticker.info.get('marketCap', 'N/A'),
        'Forward P/E': ticker.info.get('forwardPE', 'N/A'),
        'Dividend Yield': ticker.info.get('dividendYield', 'N/A'),
        'Price to Book (P/B)': ticker.info.get('priceToBook', 'N/A'),
        'Earnings Per Share (EPS)': ticker.info.get('trailingEps', 'N/A'),
        'Revenue': ticker.info.get('revenue', 'N/A'),
        'Profit Margin': ticker.info.get('profitMargins', 'N/A'),
        'Book Value': ticker.info.get('bookValue', 'N/A'),
        'Beta': ticker.info.get('beta', 'N/A'),
        '52 Week High': ticker.info.get('fiftyTwoWeekHigh', 'N/A')
    }
    
    # Technical Indicators (using simple calculations)
    hist = ticker.history(period="1y")
    sma50 = hist['Close'].rolling(window=50).mean().iloc[-1]
    sma200 = hist['Close'].rolling(window=200).mean().iloc[-1]
    
    technicals = {
        '50 Day SMA': sma50,
        '200 Day SMA': sma200,
        'Current Price': hist['Close'].iloc[-1],
        '52 Week Low': hist['Low'].min(),
        '52 Week High': hist['High'].max(),
        '1 Year Change %': ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100,
        # Add more technical indicators as needed
    }
    
    return fundamentals, technicals

def main():
    st.title("Stock Fundamental and Technical Indicators")
    
    stock = st.text_input("Enter stock ticker (e.g. AAPL):")
    
    if stock:
        fundamentals, technicals = get_data(stock)
        
        st.write("## Fundamental Indicators")
        st.write(fundamentals)
        
        st.write("## Technical Indicators")
        st.write(technicals)

if __name__ == "__main__":
    main()
