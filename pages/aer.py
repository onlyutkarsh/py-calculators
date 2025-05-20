import streamlit as st
from calculators import calculate_interest_for_periods

def clear_session():
    for key in ['amount', 'interest']:
        if key in st.session_state:
            del st.session_state[key]

def calculate_and_update_ui():
    if 'amount' not in st.session_state:
        st.session_state['amount'] = 1000.0
    if 'interest' not in st.session_state:
        st.session_state['interest'] = 4.5

    amount = float(st.session_state['amount'])
    interest = float(st.session_state['interest'])

    result = calculate_interest_for_periods(amount, interest)

    # for period, interest in result.items():
    #     st.write(f"{period} Interest: {interest:.2f}")
    print(result)
    return result


st.title("AER calculator")
# --- Clear Session Button ---
if st.button("Clear Inputs"):
    clear_session()
    st.rerun()  # Force rerun to update UI

# --- Set defaults if not in session_state ---
if 'amount' not in st.session_state:
    st.session_state['amount'] = 1000.0
if 'interest' not in st.session_state:
    st.session_state['interest'] = 4.5

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input")
    st.number_input("Amount", step=100,key="amount")
    st.number_input("Interest", step=0.01, key="interest")


with col2:
    st.subheader("Result")
    try:
        # Convert interest rate from percent to decimal
        result = calculate_interest_for_periods(
            st.session_state['amount'],
            st.session_state['interest']
        )
        for period, interest_value in result.items():
            st.write(f"{period} Interest: £{interest_value:.2f}")
    except Exception as e:
        st.error(f"Invalid input: {e}")

