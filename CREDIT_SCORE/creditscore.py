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

def get_credit_score_category(score):
    if 800 <= score <= 900:
        return "<div style='background-color: green; padding: 10px; text-align: center; border-radius: 5px;'>Exceptional</div>"
    elif 740 <= score <= 799:
        return "<div style='background-color: #ADFF2F; padding: 10px; text-align: center; border-radius: 5px;'>Very Good</div>"  # GreenYellow
    elif 670 <= score <= 739:
        return "<div style='background-color: yellow; padding: 10px; text-align: center; border-radius: 5px;'>Good</div>"
    elif 580 <= score <= 669:
        return "<div style='background-color: #FFD700; padding: 10px; text-align: center; border-radius: 5px;'>Fair</div>"  # Goldenrod
    else:
        return "<div style='background-color: red; padding: 10px; text-align: center; border-radius: 5px;'>Poor</div>"

def calculate_credit_score():
    st.markdown("""
    <style>
        .reportview-container .main .block-container {
            font-family: "Times New Roman", Times, serif;
        }
        h1, h2, h3, h4, h5, h6 {
            text-align: center;
            font-family: "Times New Roman", Times, serif;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Credit Score Calculator")
    st.write("Enter the following details to calculate your Credit score:")

    # Get user input with specified ranges
    payment_history = get_input("Percentage of timely payments (0-100): ", 0, 100)
    credit_utilization = get_input("Credit utilization ratio (0-100): ", 0, 100)
    length_of_credit_history = get_input("Length of credit history in years (e.g., 0-50): ", 0, 50)
    types_of_credit = get_input("Number of types of credit (e.g., 1-5): ", 1, 5)
    new_credit = get_input("Number of new credits opened recently (e.g., 0-10): ", 0, 10)

    # Display the "Enter" button
    if st.button('Enter'):
        # Calculate score
        score = 0
        score += payment_history * 3.5
        score += (100 - credit_utilization) * 3.0
        score += (length_of_credit_history / 50) * 150
        score += types_of_credit * 20
        score -= new_credit * 20

        # Ensure score boundaries
        score = max(300, min(900, score))

        st.markdown(f"<h2 style='text-align: center; font-family: Times New Roman, Times, serif;'>Your estimated Credit score is: {score}</h2>", unsafe_allow_html=True)
        
        # Get credit score category
        category_html = get_credit_score_category(score)
        st.markdown(category_html, unsafe_allow_html=True)
        # ... [rest of your code]

    # Dropdown for credit score improvement tips
    print()
    print()
    if st.button("How to improve your credit score"):
        st.markdown("""
        <style>
            .improve-tips {
                font-family: "Times New Roman", Times, serif;
                margin-left: 10px;
                margin-right: 10px;
            }
        </style>
        """, unsafe_allow_html=True)
    
        st.markdown("<h3 class='improve-tips'>Tips to Improve Your Credit Score</h3>", unsafe_allow_html=True)
    
        st.markdown("""
        **1. Pay Your Bills on Time:** 
        Timely payment of your bills, especially credit card bills and loan EMIs, has a significant impact on your credit score. Late payments, defaults, and bankruptcies have a negative effect on your score.

        **2. Reduce Outstanding Debt:** 
        Try to keep your credit utilization ratio low. It's the ratio of your credit card balances to their credit limits. A lower ratio indicates good credit management.

        **3. Don't Close Unused Credit Cards:** 
        Keeping unused credit cards, as long as they're not costing you money in annual fees, helps increase your credit utilization ratio.

        **4. Limit Hard Inquiries:** 
        A hard inquiry happens when a financial institution checks your credit for lending purposes. Too many hard inquiries in a short time can negatively impact your score.

        **5. Diversify Your Credit:** 
        Having a mix of credit types, such as credit cards, retail accounts, installment loans, and mortgages, can positively affect your score.

        **6. Check Your Credit Report Regularly:** 
        Ensure there are no errors or discrepancies in your credit report. If you find any, get them corrected immediately.

        **7. Avoid Taking on Too Much New Credit:** 
        Opening several credit accounts in a short period can be risky and might indicate that you're financially overextended.

        **8. Seek Professional Help:** 
        If you're overwhelmed with debt, consider seeking help from a credit counseling agency. They can provide strategies and solutions to improve your financial situation.
        """, unsafe_allow_html=True)



st.markdown("<hr/>", unsafe_allow_html=True)  # This adds a horizontal line for separation
st.markdown("<p style='text-align: center; font-family: Times New Roman, Times, serif;'>Made by Mikhdad</p>", unsafe_allow_html=True)



if __name__ == "__main__":
    calculate_credit_score()
