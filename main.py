import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

email_addresses = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']
subjects = ['Subject 1', 'Subject 2', 'Subject 3']
names = ['Name 1', 'Name 2', 'Name 3']

email_body_template = """
Dear {name},

This is a personalized email for you.

Best regards,
Your Name
"""

def send_email(to_email, subject, body):

    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
    
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        server.sendmail(SMTP_USERNAME, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

    finally:
        server.quit()

def main():
    for email, subject, name in zip(email_addresses, subjects, names):
    
        body = email_body_template.format(name=name)

        send_email(email, subject, body)

if __name__ == '__main__':
    main()
