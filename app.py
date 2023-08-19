import streamlit as st
import yfinance as yf

def get_data(stock):
    try:
        ticker = yf.Ticker(stock)

        # Check if ticker.info is a valid dictionary
        if not ticker.info or not isinstance(ticker.info, dict):
            st.error(f'Failed to fetch data for {stock}. Please try another stock ticker.')
            return {}, {}

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
            '1 Year Change %': ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
        }

        return fundamentals, technicals

    except Exception as e:
        st.error(f'An error occurred: {e}')
        return {}, {}

def main():
    st.markdown(
    """
    <style>
        .times-font {
            font-family: "Times New Roman", Times, serif;
            font-size: 28px;
            text-align: center;
            font-weight: bold;
        }
    </style>
    <div class="times-font">Analyse a stock</div>
    """, 
    unsafe_allow_html=True)

    st.markdown(
    """
    <style>
        .smaller-font {
            font-size:24px;  # adjust the size as per your requirement
            font-weight: bold;
        }
    </style>
    <div class="smaller-font">Stock Fundamental and Technical Indicators</div>
    """, 
    unsafe_allow_html=True
)

    stock = st.text_input("Enter stock ticker (e.g. AAPL):")

    if stock:
        fundamentals, technicals = get_data(stock)

        st.write("## Fundamental Indicators")

        for key, value in fundamentals.items():
            # Display each fundamental as a dropdown using native HTML details/summary tags
            st.markdown(f"""
            <details>
                <summary>{key}</summary>
                <p>{value}</p>
            </details>
            """, unsafe_allow_html=True)

        st.write("## Technical Indicators")
        st.write(technicals)

if __name__ == "__main__":
    main()
