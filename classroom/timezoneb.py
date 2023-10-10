import streamlit as st
from datetime import datetime
import pytz

st.title("Time Difference: Nigeria vs. Hong Kong")

# Define time zones
nigeria_timezone = pytz.timezone("Africa/Lagos")
hongkong_timezone = pytz.timezone("Asia/Hong_Kong")
st.write(nigeria_timezone)
st.write(hongkong_timezone)

# Get the current time for both Nigeria and Hong Kong
current_time_nigeria = datetime.now(nigeria_timezone)
current_time_hongkong = datetime.now(hongkong_timezone)
st.write

# Calculate the time difference
time_difference = current_time_hongkong - current_time_nigeria

# Display the current times and the correct time difference
st.write(f"Current Time in Nigeria: {current_time_nigeria.strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"Current Time in Hong Kong: {current_time_hongkong.strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"Time Difference (Hong Kong - Nigeria): {time_difference}")
