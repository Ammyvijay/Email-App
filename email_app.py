import os
import smtplib
import imghdr
import time
from email.message import EmailMessage
from decouple import config
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

EMAIL_ADDRESS = config('EMAIL_ADDRESS')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

msg = EmailMessage()
msg['Subject'] = 'Done Subject Header '+dt_string

msg['From'] = EMAIL_ADDRESS
msg['To'] = 'ammyvijay.b@gmail.com'
msg.set_content('Body Context\n\nThanks,\nAmmy Dev')

files = ['photo.jpeg']

for fls in files:
    with open(fls, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
