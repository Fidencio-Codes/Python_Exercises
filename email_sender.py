## Send emails with Python, using gmail


# go over to gmail account and setup 2 factor authentication 
# generate app password 
# For safety, created another file app2.py 
    # Then created a variable "password" to store google authentication 

# import EmailMessage (create: sender, receiver, subject, body)    
# Instance of message created (em)
# import SSL and smtplib
    #  This is an example of plain-text email using SMTP_SSL():
    
# create a function to send the mail
# Run program to send emails 


from email.message import EmailMessage
from app2 import password 
import ssl
import smtplib

email_sender = 'an_email@gmail.com'
email_password = password

email_receiver = 'another_email@gmail.com'

subject = "Hello World!"
body = """
I am practicing sending emails with python. How am I doing?
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject 
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())