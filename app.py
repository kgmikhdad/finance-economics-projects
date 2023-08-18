import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def get_data(stock):
    # ... [same as your code]

def main():
    st.title("Stock Fundamental and Technical Indicators")

    stock = st.text_input("Enter stock ticker (e.g. AAPL):")

    if stock:
        fundamentals, technicals = get_data(stock)

        # Using Bootstrap styling for cards
        st.markdown("""
        <style>
            .card {
                border: 1px solid #e1e4e8;
                border-radius: 6px;
                padding: 16px;
                margin: 20px 0;
            }
        </style>
        """, unsafe_allow_html=True)

        # Displaying Fundamental Indicators in a card
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("## Fundamental Indicators")
        for key, value in fundamentals.items():
            st.write(f"**{key}**: {value}")
        st.markdown("</div>", unsafe_allow_html=True)

        # Displaying Technical Indicators in a card
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("## Technical Indicators")
        for key, value in technicals.items():
            st.write(f"**{key}**: {value}")
        st.markdown("</div>", unsafe_allow_html=True)

        # Plotting some of the technical indicators
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=[technicals['50 Day SMA'], technicals['200 Day SMA'], technicals['Current Price']],
                                 x=['50 Day SMA', '200 Day SMA', 'Current Price'],
                                 mode='lines+markers'))
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
 
