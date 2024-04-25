import streamlit as st

# Get the number of items from the user
number_of_items = st.number_input(
    label="Number of Items",
    min_value=1,
    value=1,
)

# Initialize empty lists to store the items and quantities
items = []
quantities = []

# Iterate over the number of items to get the name and quantity for each item
for i in range(number_of_items):
    col1, col2 = st.columns(2)
    # Get the name of the item from the user
    with col1:
        item_name = st.text_input(
            label=f"Item {i+1}",
            key=f"item_input_{i}",
        )
    items.append(item_name)

    # Get the quantity of the item from the user
    with col2:
        quantity = st.number_input(
            label=f"Quantity {i+1}",
            key=f"quantity_input_{i}",
            min_value=0,
            max_value=100,
            value=0
        )
    quantities.append(quantity)

# Display the items and quantities
st.write("Items:", items)
st.write("Quantities:", quantities)
