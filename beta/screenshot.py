import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import pdfkit
#import tempfile  # Import tempfile module
import time  # Import time module
from PIL import Image

# Display multiline text
multiline_text = """
This is a multiline text.

It can have multiple lines.

You can format it with line breaks and whitespace as needed.

In this code:

We define a multiline text using triple quotes.
You can include line breaks and format the text as needed.

We use st.write() to display the multiline text.
Streamlit will render the text as-is, preserving the line breaks and formatting.

When you run this code, Streamlit will display the multiline text in the app.
"""

st.write(multiline_text)

# Use Chrome in headless mode (no GUI) to capture screenshots
chrome_options = Options()
chrome_options.add_argument('--headless') #this doesnt let any page show up

# Initialize ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

with st.form(key='download'):
    # Generate a unique timestamp for filenames
    timestamp = int(time.time())  # Using Unix timestamp for unique time for 
    st.write(timestamp)
    # Capture a screenshot
    screenshot_path = f"C:\\Users\\USER\\Documents\\screenshot_{timestamp}.png"

    # Create a button to save as PDF
    if st.form_submit_button("Save as PDF"):
        streamlit_url = "http://localhost:8505"  # Replace with your Streamlit app's URL
        driver.get(streamlit_url)
        # Capture a screenshot
        driver.save_screenshot(screenshot_path)

        # Open the image file
        img = Image.open(screenshot_path)
        # Create a PDF file and add the image to it
        img.save(f'screenshot_{timestamp}.pdf', 'PDF', resolution=300.0,quality=95)

        # Close the image file
        img.close()
        st.write('Done. Check Folder')

    # Close the browser
    driver.quit()
