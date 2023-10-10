import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Define the tickers for Gold and the Nifty indices
tickers = {
    'Gold': 'GLD',
    'Nifty 50': '^NSEI',
    'Nifty Auto': '^CNXAUTO',
    'Nifty Metal': '^CNXMETAL',
    'Nifty Realty': '^CNXREALTY'
}

# Fetch data from 1/11/2019 to 1/1/2021
start_date = '2019-11-01'
end_date = '2021-01-01'

data = {name: yf.download(ticker, start=start_date, end=end_date)['Close'].pct_change().dropna() + 1 
        for name, ticker in tickers.items()}

# Calculate cumulative returns
cumulative_returns = {name: returns.cumprod() for name, returns in data.items()}

def plot_portfolio(nifty50_weight, nifty_auto_weight, nifty_metal_weight, nifty_realty_weight):
    # Ensure the total weight is <= 100
    total_weight = nifty50_weight + nifty_auto_weight + nifty_metal_weight + nifty_realty_weight
    if total_weight > 100:
        st.write(f'Total weight exceeds 100%. Please adjust the weights.')
        return

    # Calculate the weight for Gold
    gold_weight = 100 - total_weight

    # Calculate portfolio returns
    portfolio_returns = (
        gold_weight / 100 * cumulative_returns['Gold'] +
        nifty50_weight / 100 * cumulative_returns['Nifty 50'] +
        nifty_auto_weight / 100 * cumulative_returns['Nifty Auto'] +
        nifty_metal_weight / 100 * cumulative_returns['Nifty Metal'] +
        nifty_realty_weight / 100 * cumulative_returns['Nifty Realty']
    )

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_returns.index, portfolio_returns, label='Portfolio')
    for name, returns in cumulative_returns.items():
        plt.plot(returns.index, returns, label=name, linestyle='dashed')
    
    plt.legend()
    plt.title('Portfolio Simulation from 1/11/2019 to 1/1/2021')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.grid(True)
    plt.show()

# Set up Streamlit sliders for asset weights
nifty50_weight = st.slider('Nifty 50 Weight', 0, 100, 20)
nifty_auto_weight = st.slider('Nifty Auto Weight', 0, 100, 20)
nifty_metal_weight = st.slider('Nifty Metal Weight', 0, 100, 20)
nifty_realty_weight = st.slider('Nifty Realty Weight', 0, 100, 20)

# Call the function when the values change
plot_portfolio(nifty50_weight, nifty_auto_weight, nifty_metal_weight, nifty_realty_weight)
