import streamlit as st

def calculate_roi(interest_rate, amount, duration, frequency):
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
    
    return total_amount

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
            </style>
        """, unsafe_allow_html=True)

    custom_css()
    st.title("ROI Calculator")

    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 5.0, 0.1)
    amount = st.number_input("Amount (₹)", min_value=100.0, max_value=10000000.0, value=1000.0, step=50.0)
    duration = st.slider("Duration (years)", 1, 40, 1)
    frequency = st.selectbox("Interest Return Frequency", ["Per Day", "Per Month", "Per Three Months", "Per Six Months", "Per Year"])

    if st.button("Calculate ROI"):
        roi = calculate_roi(interest_rate, amount, duration, frequency)
        st.write(f"Total amount after {duration} years with interest calculated {frequency.lower()}: ₹{roi:.2f}")

if __name__ == "__main__":
    main()
