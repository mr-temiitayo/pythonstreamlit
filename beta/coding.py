import streamlit as st
import pandas as pd

# Load the CSV file
csv_file_path = "dates.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Streamlit app
st.title("Categorize Amounts by Date Added")

# Get unique date values from the "Date" column
date_values = df['Date'].unique()

# Loop through unique dates and categorically display Amounts
for date in date_values:
    st.subheader(f"Amounts Added on {date}:")
    filtered_df = df[df['Date'] == date]

    # Display the Amounts for the current date
    for i, Amount in enumerate(filtered_df['Amount']):
        st.write(f"Amount {i + 1} is {Amount}")
        if i < len(filtered_df) - 1:
            st.write("----")
