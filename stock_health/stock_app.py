import streamlit as st
import yfinance as yf
import ta

def fetch_stock_data(stock_name):
    stock = yf.Ticker(stock_name)
    return stock.history(period='1y'), stock.info

def display_fundamental_data(stock_info):
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
    
    st.subheader('Fundamental Indicators')
    for indicator, value in fundamental_data.items():
        st.write(f'{indicator}: {value}')

def display_technical_indicators(hist_data):
    hist_data['MA50'] = hist_data['Close'].rolling(window=50).mean()
    hist_data['EMA50'] = hist_data['Close'].ewm(span=50, adjust=False).mean()
    macd = ta.trend.MACD(hist_data['Close'])
    hist_data['MACD'] = macd.macd()
    rsi = ta.momentum.RSIIndicator(hist_data['Close'])
    hist_data['RSI'] = rsi.rsi()
    bollinger = ta.volatility.BollingerBands(hist_data['Close'])
    hist_data['Bollinger High'] = bollinger.bollinger_hband()
    hist_data['Bollinger Low'] = bollinger.bollinger_lband()
    stochastic = ta.momentum.StochasticOscillator(hist_data['High'], hist_data['Low'], hist_data['Close'])
    hist_data['Stochastic Oscillator'] = stochastic.stoch()
    atr = ta.volatility.AverageTrueRange(hist_data['High'], hist_data['Low'], hist_data['Close'])
    hist_data['ATR'] = atr.average_true_range()
    parabolic_sar = ta.trend.PSARIndicator(hist_data['High'], hist_data['Low'], hist_data['Close'])
    hist_data['Parabolic SAR'] = parabolic_sar.psar()

    st.subheader('Technical Indicators')
    st.write(f'Moving Average (MA): {hist_data["MA50"].iloc[-1]}')
    st.write(f'Exponential Moving Average (EMA): {hist_data["EMA50"].iloc[-1]}')
    st.write(f'MACD: {hist_data["MACD"].iloc[-1]}')
    st.write(f'RSI: {hist_data["RSI"].iloc[-1]}')
    st.write(f'Bollinger Bands: {hist_data["Bollinger High"].iloc[-1]} (High), {hist_data["Bollinger Low"].iloc[-1]} (Low)')
    st.write(f'Stochastic Oscillator: {hist_data["Stochastic Oscillator"].iloc[-1]}')
    st.write(f'ATR: {hist_data["ATR"].iloc[-1]}')
    st.write(f'Parabolic SAR: {hist_data["Parabolic SAR"].iloc[-1]}')

def main():
    st.title('Stock Indicators App')
    stock_name = st.text_input('Enter the stock name (e.g. AAPL for Apple): ')

    if stock_name:
        hist_data, stock_info = fetch_stock_data(stock_name)
        
        if hist_data.empty:
            st.error(f"No data available for {stock_name}. Please enter a valid stock ticker.")
            return
        
        display_fundamental_data(stock_info)
        display_technical_indicators(hist_data)

if __name__ == "__main__":
    main()
