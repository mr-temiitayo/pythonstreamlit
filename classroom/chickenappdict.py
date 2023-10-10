import streamlit as st

# Title
st.title("Chicken Order App")

# Interactive Form
st.subheader("Chicken Order Form")

# Form inputs
chicken_type = st.selectbox("Select chicken type:", ["Whole Chicken", "Chicken Wings", "Chicken Drumsticks"])
quantity = st.number_input("Enter quantity:", min_value=1, value=1)
price_per_unit = {
    "Whole Chicken": 10.00,
    "Chicken Wings": 5.00,
    "Chicken Drumsticks": 8.00,
}
total_cost = quantity * price_per_unit[chicken_type]

# Calculate total cost
st.write(f"Total Cost: ${total_cost:.2f}")

# Display Order Summary
st.subheader("Order Summary")
st.write("You have ordered:")
st.write(f"- {quantity} {chicken_type}")
st.write(f"- Total Cost: ${total_cost:.2f}")
