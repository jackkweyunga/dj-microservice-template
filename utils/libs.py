import smtplib
from django.conf import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#send email input: subject, message, to_email
def send_email(subject, message, to_email):
    sender_email = settings.MAIL_SENDER_EMAIL
    sender_password = settings.MAIL_SENDER_PASSWORD
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server.send_message(msg)
        print("Email sent successfully", to_email)
    except Exception as e:
        print(e)
    finally:
        server.quit()


