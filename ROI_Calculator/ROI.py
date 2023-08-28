import streamlit as st

def calculate_roi(interest_rate, amount, duration):
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

    if st.button("Calculate ROI"):
        roi = calculate_roi(interest_rate, amount, duration)
        st.write(f"Total amount after {duration} years: ₹{roi:.2f}")

if __name__ == "__main__":
    main()
