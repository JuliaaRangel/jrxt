# go to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send the email
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rangeltjul@gmail.com'
email_password = 'miadqpkdggdawutu'

email_receiver = 'pimecic574@cebaike.com'

subject = "Learning Python"
body = """
If you got this email, the program works!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp :
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
