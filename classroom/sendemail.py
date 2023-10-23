import streamlit as st
import smtplib

# Replace with your Gmail account credentials
EMAIL_ADDRESS = "githubtee@gmail.com"
EMAIL_PASSWORD = "cczaelfrzzyywngz"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(recipient, subject, message):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_ADDRESS, recipient, msg)

recipient = "teeakintoye@yahoo.com" #st.text_input("Recipient Email:",key='rep')
subject = "VSCODE TEST" #st.text_input("Email Subject:",key='sub')
message = st.text_area("Email Message:",key='mess')

if st.button("Send Email"):
    send_email(recipient, subject, message)
    st.success("Email sent successfully!")
