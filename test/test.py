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

def adjust_for_inflation(amount, inflation_rate, duration):
    return amount / ((1 + inflation_rate / 100) ** duration)

# ... [rest of the code remains the same]

if st.button("Calculate ROI"):
    roi = calculate_roi(interest_rate, amount, duration, frequency)
    roi_adjusted = adjust_for_inflation(roi, inflation_rate, duration)
    st.write(f"Investing in {selected_instrument}, the total amount after {duration} years with interest calculated {frequency.lower()} (adjusted for inflation) will be: ₹{roi_adjusted:.2f}")
