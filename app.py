import streamlit as st
import util

st.title("Bangalore Home Price Prediction")

st.write("Enter the details below to get the estimated home price:")

util.load_saved_artifacts()
locations = util.get_location_names()

total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
location = st.selectbox("Location", locations)
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])
bath = st.selectbox("Bathroom", [1, 2, 3, 4, 5])

if st.button("Predict Price"):
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    st.write(f"The estimated price for the house is: ₹{estimated_price} Lakhs")
