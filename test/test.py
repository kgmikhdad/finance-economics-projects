import streamlit as st

def tradingview_widget():
    html_code = """
    <div class="tradingview-widget-container">
      <div id="tradingview_da31d"></div>
      <div class="tradingview-widget-copyright">
        <a href="https://in.tradingview.com/" rel="noopener nofollow" target="_blank">
          <span class="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {
      "autosize": true,
      "symbol": "NASDAQ:AAPL",
      "interval": "D",
      "timezone": "Etc/UTC",
      "theme": "light",
      "style": "1",
      "locale": "in",
      "enable_publishing": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_da31d"
      }
      );
      </script>
    </div>
    """
    st.components.v1.html(html_code, height=600)

st.title("TradingView Widget in Streamlit")
tradingview_widget()
