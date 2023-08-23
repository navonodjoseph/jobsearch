# email_sender.py
import os 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_encouraging_email(application_position, recipient_email):
    sender_email = os.environ.get('joedonovan46@gmail.com')
    sender_password = os.environ.get('zgzexivbotexofkj')


    msg = MIMEMultipart()
    msg['From'] = 'Joe Donovan'
    msg['To'] = 'joepeterdonovan@gmail.com'
    msg['Subject'] = 'Encouraging Message for Your Job Application'

    body = f"Hello!\n\nYou applied for the position: {application_position}. Keep up the great work!"
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
