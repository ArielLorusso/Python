import os
import ssl
import smtplib
from   email.message import EmailMessage
from   datetime      import datetime, timedelta

# Set variables:
email_sender = 'ariellorusso@gmail.com'
email_password = 'csXX XXXX XXXX XXef'    # https://mail.google.com/mail/u/0/#inbox/FMfcgzGxSRSCbVrsDGNNJfXqZQPMptsv
# https://myaccount.google.com/apppasswords
# this is because i have 2 step authentication
email_receiver = 'ariellorusso@gmail.com'
subject = 'Automatic test code'
body = """ 

I've just send myself a mail automatically
"""
script_dir      = os.path.dirname(os.path.abspath(__file__))
attachment_name = 'dummy.pdf'
attachment_path = os.path.join(script_dir, attachment_name)

# Get Datetime
future_time_1    = datetime.now() + timedelta( minutes=1 ) # hours= , days= 
# future_time_2 = datetime(2024, 12, 21, 22, 0, 0)   #  21/dec/2024 22 hs 0 min
future_unixtime = int(future_time_1.timestamp())
body += future_time_1.strftime("%Y-%m-%d %H:%M:%S")

def sendEmail():
    # fill email object's content:
    em = EmailMessage()
    em['From']    = email_sender
    em['To']      = email_receiver
    em['Subject'] = subject
    em.set_content (body)

    # Attach the file
    with open( attachment_path , 'rb') as f:
        file_data = f.read()
        em.add_attachment(file_data, maintype='application', 
                        subtype='octet-stream', filename='book.pdf')

    # Send email:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #                 host:smtp.gmail.com   port:465     context: SSLContext
        smtp.login   (email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return

while(1):
    current_datetime = datetime.now()
    current_unixtime = int(current_datetime.timestamp())
    
    if current_unixtime > future_unixtime :
        print("sending")
        sendEmail()
        print("email sent")
        break
