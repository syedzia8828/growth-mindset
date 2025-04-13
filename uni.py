import streamlit as st
import io  


def convert_units(value, unit_from, unit_to):


    conversions = {

        "meter_kilometer" : 0.001,
        "kilometer_meter" : 1000,
        "gram_kilogram" : 0.001,
        "kilogram_gram" : 1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "conversion not support"
    
st.title("Unit_Converter")

value = st.number_input("Enter the value:")

unit_from = st.selectbox("Converter from:", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilometer "])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")
