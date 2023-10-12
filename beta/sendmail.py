import streamlit as st
import smtplib

def send_email(to_email, subject, message):
  """Sends an email.

  Args:
    to_email: The email address of the recipient.
    subject: The subject of the email.
    message: The body of the email.
  """

  # Create an SMTP object.
  smtp_obj = smtplib.SMTP("smtp.mail.yahoo.com", 587)

  # Start TLS encryption.
  smtp_obj.starttls()

  # Login to the SMTP server.
  smtp_obj.login("sender@example.com", "password")

  # Create a MIME message object.
  msg = smtplib.SMTP.MIME_MESSAGE()
  msg["From"] = "sender@example.com"
  msg["To"] = to_email
  msg["Subject"] = subject
  msg.attach(smtplib.SMTP.MIME_TEXT(message))

  # Send the email.
  smtp_obj.send_message(msg)

  # Close the SMTP object.
  smtp_obj.quit()

# Create a form.
form = st.form("Send email")

# Add an input field for the email address of the recipient.
to_email = form.text_input("To email:")

# Add an input field for the subject of the email.
subject = form.text_input("Subject:")

# Add a text area for the body of the email.
message = form.text_area("Message:")

# Submit the form.
submitted = form.form_submit_button("Send")

# If the form is submitted, send the email.
if submitted:
  send_email(to_email, subject, message)

# If the email is sent successfully, display a success message.
