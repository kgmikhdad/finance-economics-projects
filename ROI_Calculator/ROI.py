import streamlit as st

# Function to calculate ROI
def calculate_roi(interest_rate, amount, duration):
    total_amount = amount * ((1 + (interest_rate / 100)) ** duration)
    return total_amount

# Streamlit app
def main():
    # Custom CSS for centering the title and setting the font style
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

    # User input
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, 5.0, 0.1)
    amount = st.slider("Amount (₹)", 100.0, 10000.0, 1000.0, 50.0)
    duration = st.slider("Duration (years)", 1, 10, 1)

    # Calculate ROI
    if st.button("Calculate ROI"):
        roi = calculate_roi(interest_rate, amount, duration)
        st.write(f"Total amount after {duration} years: ₹{roi:.2f}")

if __name__ == "__main__":
    main()
