# app.py
import yfinance as yf
import streamlit as st
import ta

def fetch_data(ticker_symbol):
    # Fetch data
    df = yf.download(ticker_symbol, period="1y")
    
    # Fetch additional info for the stock
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    # Fundamental indicators
    fundamentals = {
        'Open': df['Open'].iloc[-1],
        'High': df['High'].iloc[-1],
        'Low': df['Low'].iloc[-1],
        'Close': df['Close'].iloc[-1],
        'Volume': df['Volume'].iloc[-1],
        'Dividends': df['Dividends'].iloc[-1],
        'Market Cap': info.get('marketCap', 'N/A'),
        'Dividend Yield': info.get('dividendYield', 'N/A'),
        'Forward PE': info.get('forwardPE', 'N/A'),
        'Trailing PE': info.get('trailingPE', 'N/A')
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
