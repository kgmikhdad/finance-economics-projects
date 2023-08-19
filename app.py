def main():
    st.markdown(
    """
    <style>
        .times-font {
            font-family: "Times New Roman", Times, serif;
            font-size: 30px;
            text-align: center;
            font-weight: bold;
        }
    </style>
    <div class="times-font">Analyse a stock</div>
    """, 
    unsafe_allow_html=True)

    stock = st.text_input("Enter stock ticker (e.g. AAPL):")

    if stock:
        fundamentals, technicals = get_data(stock)

        # Create two columns to display data side by side
        col1, col2 = st.beta_columns(2)

        with col1:
            st.write("## Fundamental Indicators")
            for key, value in fundamentals.items():
                # Display each fundamental as a dropdown using native HTML details/summary tags
                st.markdown(f"""
                <details>
                    <summary>{key}</summary>
                    <p>{value}</p>
                </details>
                """, unsafe_allow_html=True)
        
        with col2:
            st.write("## Technical Indicators")
            for key, value in technicals.items():
                # Display each technical indicator as a dropdown using native HTML details/summary tags
                st.markdown(f"""
                <details>
                    <summary>{key}</summary>
                    <p>{value}</p>
                </details>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
