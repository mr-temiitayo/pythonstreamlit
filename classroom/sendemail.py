
from email.message import EmailMessage
import ssl #for secure connection between mails to ensure your username & password is secured
import smtplib #Simple Mail Transfer Protocol

email_sender = "Temitayo"
email_password = "cczaelfrzzyywngz"
email_receiver = "teeakintoye@yahoo.com"

subject = "Email From VSCode"
body = """
Here is the mail to check your work
"""


# The EmailMessage is a keyword in the email library, 
# to configure & the email
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body) #set_content means the main message



context = ssl.create_default_context() #ensures email content is secured
#hostname, port,ssl

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    #em.as_string() convert your config to strings

