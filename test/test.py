import streamlit as st

def tradingview_widget(stock_symbol):
    html_code = f"""
    <div class="tradingview-widget-container" style="width: 100%; height: 100%;">
      <div id="tradingview_da31d" style="width: 100%; height: 100%;"></div>
      <div class="tradingview-widget-copyright">
        <a href="https://in.tradingview.com/" rel="noopener nofollow" target="_blank">
          <span class="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {{
      "autosize": true,
      "symbol": "{stock_symbol}",
      "interval": "D",
      "timezone": "Etc/UTC",
      "theme": "light",
      "style": "1",
      "locale": "in",
      "enable_publishing": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_da31d"
      }}
      );
      </script>
    </div>
    """
    st.components.v1.html(html_code, height=800, width=1200)

st.title("TradingView Widget in Streamlit")

# User input for stock symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g. NASDAQ:AAPL):", "NASDAQ:AAPL").upper()

if stock_symbol:
    tradingview_widget(stock_symbol)
