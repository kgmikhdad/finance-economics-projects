import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

st.title('Portfolio Simulation from 2019-11-01 to 2021-01-01')

gold_ticker = 'GLD'
nifty_pharma_ticker = '^CRSLDX'
nifty_fmcg_ticker = '^CNXFMCG'
nifty_bank_ticker = '^NSEBANK'
nifty_it_ticker = '^CNXIT'

start_date = '2019-11-01'
end_date = '2021-01-01'

gold_data = yf.download(gold_ticker, start=start_date, end=end_date)
nifty_pharma_data = yf.download(nifty_pharma_ticker, start=start_date, end=end_date)
nifty_fmcg_data = yf.download(nifty_fmcg_ticker, start=start_date, end=end_date)
nifty_bank_data = yf.download(nifty_bank_ticker, start=start_date, end=end_date)
nifty_it_data = yf.download(nifty_it_ticker, start=start_date, end=end_date)

gold_returns = gold_data["Close"].pct_change().dropna() + 1
nifty_pharma_returns = nifty_pharma_data["Close"].pct_change().dropna() + 1
nifty_fmcg_returns = nifty_fmcg_data["Close"].pct_change().dropna() + 1
nifty_bank_returns = nifty_bank_data["Close"].pct_change().dropna() + 1
nifty_it_returns = nifty_it_data["Close"].pct_change().dropna() + 1

gold_cumulative_returns = gold_returns.cumprod()
nifty_pharma_cumulative_returns = nifty_pharma_returns.cumprod()
nifty_fmcg_cumulative_returns = nifty_fmcg_returns.cumprod()
nifty_bank_cumulative_returns = nifty_bank_returns.cumprod()
nifty_it_cumulative_returns = nifty_it_returns.cumprod()

gold_weight = st.sidebar.slider('gold weight', 0.0, 1.0, 0.2)
nifty_pharma_weight = st.sidebar.slider('nifty pharma weight', 0.0, 1.0, 0.2)
nifty_fmcg_weight = st.sidebar.slider('nifty fmcg weight', 0.0, 1.0, 0.2)
nifty_bank_weight = st.sidebar.slider('nifty bank weight', 0.0, 1.0, 0.2)
nifty_it_weight = 1 - gold_weight - nifty_pharma_weight - nifty_fmcg_weight - nifty_bank_weight

portfolio_returns = gold_weight * gold_cumulative_returns + nifty_pharma_weight * nifty_pharma_cumulative_returns + nifty_fmcg_weight * nifty_fmcg_cumulative_returns + nifty_bank_weight * nifty_bank_cumulative_returns + nifty_it_weight * nifty_it_cumulative_returns

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(portfolio_returns.index, portfolio_returns, label=f'Portfolio')
ax.plot(gold_cumulative_returns.index, gold_cumulative_returns, label='Gold', linestyle='dashed')
ax.plot(nifty_pharma_cumulative_returns.index, nifty_pharma_cumulative_returns, label='Nifty Pharma', linestyle='dashed')
ax.plot(nifty_fmcg_cumulative_returns.index, nifty_fmcg_cumulative_returns, label='Nifty FMCG', linestyle='dashed')
ax.plot(nifty_bank_cumulative_returns.index, nifty_bank_cumulative_returns, label='Nifty Bank', linestyle='dashed')
ax.plot(nifty_it_cumulative_returns.index, nifty_it_cumulative_returns, label='Nifty IT', linestyle='dashed')
ax.legend()
ax.grid(True)
st.pyplot(fig)
