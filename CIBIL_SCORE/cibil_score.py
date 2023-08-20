#This is a python code for calculating CIBIL Score.
#This python script can be run using streamlit in the form of website.
import streamlit as st

def get_input(prompt, min_val, max_val):
    try:
        value = st.number_input(prompt, min_value=min_val, max_value=max_val)
        if min_val <= value <= max_val:
            return value
        else:
            st.warning(f"Please enter a value between {min_val} and {max_val}.")
            return get_input(prompt, min_val, max_val)
    except ValueError:
        st.warning("Please enter a valid number.")
        return get_input(prompt, min_val, max_val)

def calculate_cibil_score():
    st.title("CIBIL Score Calculator")
    st.write("Enter the following details to calculate your CIBIL score:")

    # Get user input with specified ranges
    payment_history = get_input("Percentage of timely payments (0-100): ", 0, 100)
    credit_utilization = get_input("Credit utilization ratio (0-100): ", 0, 100)
    length_of_credit_history = get_input("Length of credit history in years (e.g., 0-50): ", 0, 50)
    types_of_credit = get_input("Number of types of credit (e.g., 1-5): ", 1, 5)
    new_credit = get_input("Number of new credits opened recently (e.g., 0-10): ", 0, 10)

    # Calculate score
    score = 0
    score += payment_history * 0.35
    score += (100 - credit_utilization) * 0.30  # Lower utilization is better
    score += (length_of_credit_history / 10) * 15  # Assuming 10+ years is best
    score += types_of_credit * 2  # Assuming 5 types is best
    score -= new_credit * 2  # Assuming 0 new credit is best

    # Ensure score boundaries
    score = max(300, min(900, score * 10))

    st.success(f"Your estimated CIBIL score is: {score}")

if __name__ == "__main__":
    calculate_cibil_score()