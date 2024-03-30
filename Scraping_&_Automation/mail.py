import os
import smtplib
import ssl
from email.message import EmailMessage

# Set variables:
email_sender   = 'myEmail@gmail.com'
email_password = 'my_password'    # or   app_password 
# https://myaccount.google.com/apppasswords?
# 2 step authentication user must create app_password
email_receiver = 'theirEmail@gmail.com'
subject = 'Automatic test code'
body    = """ 
I've just send miself a mail automatically
"""

# fill email object's content:
em = EmailMessage()
em['From']    = email_sender
em['To']      = email_receiver
em['Subject'] = subject
em.set_content (body)

# Attach the PDF file
script_dir    = os.path.dirname(os.path.abspath(__file__))
pdf_file_path = os.path.join(script_dir, 'dummy.pdf')

with open( pdf_file_path , 'rb') as f:
    pdf_data = f.read()
    em.add_attachment(pdf_data, maintype='application', 
                      subtype='octet-stream', filename='book.pdf')


# Send email:
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#                 host:smtp.gmail.com   port:465     context: SSLContext
    smtp.login   (email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())