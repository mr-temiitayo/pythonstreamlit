import streamlit as st
from datetime import datetime, timedelta
import pytz

st.title("Nigeria Time to London Time Converter")

# Input field for Nigeria time
nigeria_time = st.time_input("Enter Nigeria Time:",step=60*60)
# step=60*60 seconds = 1 hour
# step=30*60 seconds = 30 minutes
if st.button("Convert"):
    if nigeria_time:
        # Define time zones
        nigeria_timezone = pytz.timezone("Africa/Lagos")
        london_timezone = pytz.timezone("Europe/London")

        # Get the current date and time
        current_datetime = datetime.now()

        st.write(current_datetime)

        # Combine the input Nigeria time with the current date and Nigeria timezone
        nigeria_datetime = nigeria_timezone.localize(datetime.combine(current_datetime.date(), nigeria_time))

        # Calculate the London time by adding 1 hour (1-hour interval)
        london_datetime = nigeria_datetime + timedelta(hours=1)

        # Display the converted London time
        st.success(f"London Time: {london_datetime.strftime('%H:%M:%S')}")
    else:
        st.warning("Please enter Nigeria time.")
