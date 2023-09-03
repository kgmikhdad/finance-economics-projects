import streamlit as st

def calculate_roi(interest_rate, amount, duration, frequency, tax_rate=0):
    # Initial ROI calculation without tax
    if frequency == "Per Day":
        total_days = duration * 365
        total_amount = amount * ((1 + (interest_rate / (100 * 365))) ** total_days)
    elif frequency == "Per Month":
        total_months = duration * 12
        total_amount = amount * ((1 + (interest_rate / (100 * 12))) ** total_months)
    elif frequency == "Per Three Months":
        total_quarters = duration * 4
        total_amount = amount * ((1 + (interest_rate / (100 * 4))) ** total_quarters)
    elif frequency == "Per Six Months":
        total_half_years = duration * 2
        total_amount = amount * ((1 + (interest_rate / (100 * 2))) ** total_half_years)
    else:  # Per Year
        total_amount = amount * ((1 + (interest_rate / 100)) ** duration)

    # Deducting tax annually from the profit
    annual_profit = total_amount - amount
    annual_profit_after_tax = annual_profit * (1 - tax_rate / 100)
    total_amount_after_tax = amount + annual_profit_after_tax

    return total_amount, total_amount_after_tax

def adjust_for_inflation(amount, inflation_rate, duration):
    return amount / ((1 + inflation_rate / 100) ** duration)

def main():
    def custom_css():
        st.markdown("""
            <style>
                h1 {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: 'Times New Roman', Times, serif;
                }
                .stApp > div > div > div > div {
                    align-items: center;
                }
            </style>
        """, unsafe_allow_html=True)

    custom_css()
    st.title("ROI Calculator")

    financial_instruments = [
        "Bonds", "Certificates of Deposit (CDs)", "Stocks", "Fixed Annuities", 
        "Money Market Instruments", "Treasury Bills", "Commercial Paper", 
        "Bankers' Acceptances", "Mortgage-Backed Securities (MBS)", 
        "Collateralized Debt Obligations (CDOs)", "Fixed Rate Loan Notes"
    ]
    
    selected_instrument = st.selectbox("Select Financial Instrument", financial_instruments)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 5.0, 0.1)
    inflation_rate = st.slider("Inflation Rate (%)", 0.0, 10.0, 2.0, 0.1)
    tax_rate = st.slider("Tax Rate (%)", 0.0, 50.0, 25.0, 0.1)
    amount = st.number_input("Amount (₹)", min_value=100.0, max_value=10000000.0, value=1000.0, step=50.0)
    duration = st.slider("Duration (years)", 1, 40, 1)
    frequency = st.selectbox("Interest Return Frequency", ["Per Day", "Per Month", "Per Three Months", "Per Six Months", "Per Year"])

    if st.button("Calculate ROI"):
        roi, roi_after_tax = calculate_roi(interest_rate, amount, duration, frequency, tax_rate)
        roi_adjusted = adjust_for_inflation(roi, inflation_rate, duration)
        roi_after_tax_adjusted = adjust_for_inflation(roi_after_tax, inflation_rate, duration)
        
        st.write(f"Investing in {selected_instrument}, the total amount after {duration} years with interest calculated {frequency.lower()} (adjusted for inflation) will be: ₹{roi_adjusted:.2f}")
        st.write(f"After deducting the tax, the total amount will be: ₹{roi_after_tax_adjusted:.2f}")
        
        # Graphical representation of ROI over time
        years = list(range(1, duration + 1))
        roi_values = [adjust_for_inflation(calculate_roi(interest_rate, amount, year, frequency, tax_rate)[1], inflation_rate, year) for year in years]
        st.line_chart({"ROI After Tax": roi_values}, use_container_width=True)

if __name__ == "__main__":
    main()
