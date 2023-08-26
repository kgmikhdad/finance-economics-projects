# app.py
import pandas_datareader as web
import streamlit as st
import ta
import datetime

def fetch_data(ticker_symbol):
    # Set the end date to today and the start date to one year ago
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=365)
    
    # Fetch data
    df = web.DataReader(ticker_symbol, 'yahoo', start, end)
    
    # Fundamental indicators
    fundamentals = {
        'Open': df['Open'].iloc[-1],
        'High': df['High'].iloc[-1],
        'Low': df['Low'].iloc[-1],
        'Close': df['Close'].iloc[-1],
        'Volume': df['Volume'].iloc[-1],
        'Adj Close': df['Adj Close'].iloc[-1],
        # Add other available indicators...
    }

    # Technical indicators using the `ta` library
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['MACD'] = ta.trend.MACD(df['Close']).macd()
    df['BB_High'] = ta.volatility.BollingerBands(df['Close']).bollinger_hband()
    df['BB_Low'] = ta.volatility.BollingerBands(df['Close']).bollinger_lband()
    df['Stochastic Oscillator'] = ta.momentum.StochasticOscillator(df['High'], df['Low'], df['Close']).stoch()
    df['ATR'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close']).average_true_range()
    df['MFI'] = ta.momentum.MFIIndicator(df['High'], df['Low'], df['Close'], df['Volume']).money_flow_index()
    df['ADX'] = ta.trend.ADXIndicator(df['High'], df['Low'], df['Close']).adx()
    df['CCI'] = ta.trend.CCIIndicator(df['High'], df['Low'], df['Close']).cci()
    df['PPO'] = ta.momentum.PercentagePriceOscillator(df['Close']).ppo()

    technicals = {
        'RSI': df['RSI'].iloc[-1],
        'MACD': df['MACD'].iloc[-1],
        'Bollinger Band High': df['BB_High'].iloc[-1],
        'Bollinger Band Low': df['BB_Low'].iloc[-1],
        'Stochastic Oscillator': df['Stochastic Oscillator'].iloc[-1],
        'Average True Range (ATR)': df['ATR'].iloc[-1],
        'Money Flow Index (MFI)': df['MFI'].iloc[-1],
        'ADX': df['ADX'].iloc[-1],
        'Commodity Channel Index (CCI)': df['CCI'].iloc[-1],
        'Percentage Price Oscillator (PPO)': df['PPO'].iloc[-1]
    }
    
    return fundamentals, technicals

st.title('Stock Indicators App')

ticker_symbol = st.text_input('Enter Ticker Symbol:', value='AAPL').upper()

if st.button('Fetch Data'):
    fundamentals, technicals = fetch_data(ticker_symbol)
    st.write('## Fundamental Indicators')
    st.write(fundamentals)
    
    st.write('## Technical Indicators')
    st.write(technicals)

# For running the app, in the terminal use:
# streamlit run app.py
