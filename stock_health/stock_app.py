import streamlit as st
import yfinance as yf
import ta

def display_stock_indicators(stock_name):
    # Fetch data
    stock = yf.Ticker(stock_name)
    hist_data = stock.history(period='1y')
    
    # Check if data was fetched successfully
    if hist_data.empty:
        st.write(f"No data available for {stock_name}. Please enter a valid stock ticker.")
        return
    
    # Fundamental Indicators
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
    
    # Display the fundamental indicators
    st.subheader(f'Fundamental Indicators for {stock_name}')
    for indicator, value in fundamental_data.items():
        st.write(f'{indicator}: {value}')
    
    # Technical Indicators
    # Moving Average (MA) for the last 50 days
    hist_data['MA50'] = hist_data['Close'].rolling(window=50).mean()
    # Exponential Moving Average (EMA) for the last 50 days
    hist_data['EMA50'] = hist_data['Close'].ewm(span=50, adjust=False).mean()
    # MACD
    macd = ta.trend.MACD(hist_data['Close'])
    hist_data['MACD'] = macd.macd()
    # RSI
    rsi = ta.momentum.RSIIndicator(hist_data['Close'])
    hist_data['RSI'] = rsi.rsi()
    # Bollinger Bands
    bollinger = ta.volatility.BollingerBands(hist_data['Close'])
    hist_data['Bollinger High'] = bollinger.bollinger_hband()
    hist_data['Bollinger Low'] = bollinger.bollinger_lband()
    # Stochastic Oscillator
    stochastic = ta.momentum.StochasticOscillator(hist_data['High'], hist_data['Low'], hist_data['Close'])
    hist_data['Stochastic Oscillator'] = stochastic.stoch()
    # Average True Range (ATR)
    atr = ta.volatility.AverageTrueRange(hist_data['High'], hist_data['Low'], hist_data['Close'])
    hist_data['ATR'] = atr.average_true_range()
    # Parabolic SAR (Stop and Reverse)
    parabolic_sar = ta.trend.PSARIndicator(hist_data['High'], hist_data['Low'], hist_data['Close'])
    hist_data['Parabolic SAR'] = parabolic_sar.psar()

    # Display the technical indicators
    st.subheader(f'Technical Indicators for {stock_name}')
    st.write(f'Moving Average (MA): {hist_data["MA50"].iloc[-1]}')
    st.write(f'Exponential Moving Average (EMA): {hist_data["EMA50"].iloc[-1]}')
    st.write(f'Moving Average Convergence Divergence (MACD): {hist_data["MACD"].iloc[-1]}')
    st.write(f'Relative Strength Index (RSI): {hist_data["RSI"].iloc[-1]}')
    st.write(f'Bollinger Bands: {hist_data["Bollinger High"].iloc[-1]} (High), {hist_data["Bollinger Low"].iloc[-1]} (Low)')
    st.write(f'Stochastic Oscillator: {hist_data["Stochastic Oscillator"].iloc[-1]}')
    st.write(f'Average True Range (ATR): {hist_data["ATR"].iloc[-1]}')
    st.write(f'Parabolic SAR (Stop and Reverse): {hist_data["Parabolic SAR"].iloc[-1]}')

# Streamlit UI
st.title('Stock Indicators App')
stock_name = st.text_input('Enter the stock name (e.g. AAPL for Apple): ')

if stock_name:
    display_stock_indicators(stock_name)
