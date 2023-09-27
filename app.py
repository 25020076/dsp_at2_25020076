import streamlit as st

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import format_output

# Display Streamlit App Title
st.title("FX Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if not currencies:
    st.error("Error fetching available currencies!")
else:
    # Add input fields for capturing amount, from and to currencies
    amount = st.number_input("Amount to be converted", min_value=0.0)
    from_currency = st.selectbox("From Currency", currencies)
    to_currency = st.selectbox("To Currency", currencies)

    # Add a button to get and display the latest rate for selected currencies and amount
    if from_currency == to_currency:
        st.warning("Conversion between the same currency pair is trivial.")
    else:
        if st.button("Get Latest Rate"):
            date, rate = get_latest_rates(from_currency, to_currency)
            if date and rate:
                output = format_output(date, from_currency, to_currency, rate, amount)
                st.text(output)

    # Add a date selector (calendar)
    selected_date = st.date_input("Select date")

    # Add a button to get and display the historical rate for selected date, currencies and amount
    if st.button("Get Historical Rate"):
        historical_rate = get_historical_rate(from_currency, to_currency, selected_date)
        if historical_rate:
            output = format_output(str(selected_date), from_currency, to_currency, historical_rate, amount)
            st.text(output)