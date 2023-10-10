import streamlit as st
import requests

# Streamlit app title and header
st.title("Temporary Email Sender")
st.header("Send an Email using Temporary Email Service")

# Input fields for sender and recipient details
sender_email = st.text_input("Your Email Address")
recipient_email = st.text_input("Recipient's Email Address")
subject = st.text_input("Subject")
message = st.text_area("Message")

# Send email button
if st.button("Send Email"):
    # API endpoint for temporary email service
    api_url = "https://api.temp-mail.org/request/mail/id"

    # Generate a random email address
    response = requests.get(api_url)
    email_data = response.json()
    temp_email = email_data['email']

    # API endpoint for sending email
    send_url = "https://api.temp-mail.org/request/mail/id/" + temp_email

    # Email payload
    email_payload = {
        "sender": sender_email,
        "recipient": recipient_email,
        "subject": subject,
        "message": message
    }

    # Send email using temporary email service
    response = requests.post(send_url, json=email_payload)
    if response.status_code == 200:
        st.success("Email sent successfully!")
    else:
        st.error("Failed to send email. Please try again.")

    # Display the temporary email address
    st.subheader("Temporary Email Address")
    st.write(temp_email)