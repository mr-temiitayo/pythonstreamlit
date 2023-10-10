import streamlit as st

st.title("Daily Savings Calculator")

# Initialize a dictionary to store daily savings
savings = {
    "Sunday": 0,
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
}

# Ask the user for daily savings
for day in savings.keys():
    savings[day] = st.number_input(f"Enter savings for {day}:", min_value=0)

# Calculate the total savings for the week
total_savings = sum(savings.values())

# Display the total savings
st.write(f"Total savings for the week: ${total_savings}")



# import streamlit as st

# st.title("Daily Savings Calculator")

# # Ask the user for daily savings for each day of the week
# sunday_savings = st.number_input("Enter savings for Sunday:", min_value=0)
# monday_savings = st.number_input("Enter savings for Monday:", min_value=0)
# tuesday_savings = st.number_input("Enter savings for Tuesday:", min_value=0)
# wednesday_savings = st.number_input("Enter savings for Wednesday:", min_value=0)
# thursday_savings = st.number_input("Enter savings for Thursday:", min_value=0)
# friday_savings = st.number_input("Enter savings for Friday:", min_value=0)
# saturday_savings = st.number_input("Enter savings for Saturday:", min_value=0)

# # Calculate the total savings for the week
# total_savings = (
#     sunday_savings
#     + monday_savings
#     + tuesday_savings
#     + wednesday_savings
#     + thursday_savings
#     + friday_savings
#     + saturday_savings
# )

# # Display the total savings
# st.write(f"Total savings for the week: ${total_savings}")
