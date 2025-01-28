import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('PASSWORD')

email_addresses = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']
subjects = ['Subject 1', 'Subject 2', 'Subject 3']
names = ['Name 1', 'Name 2', 'Name 3']

email_body_template = """
Here is email body.
"""


def send_email(to_email, subject, body):
    print(f"Sending email to: {to_email}")
    print(f"Subject: {subject}")

    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:

        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)


        server.sendmail(SMTP_USERNAME, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

    finally:

        server.quit()

def main():
    resume_link = os.getenv('RESUME_LINK')
    linkedin_link = os.getenv('LINKEDIN_LINK')
    github_link = os.getenv('GITHUB_LINK')


    # Debug print statements
    print(f"SMTP_USERNAME: {SMTP_USERNAME}")
    print(f"SMTP_PASSWORD: {SMTP_PASSWORD}")
    print(f"RESUME_LINK: {resume_link}")
    print(f"LINKEDIN_LINK: {linkedin_link}")
    print(f"GITHUB_LINK: {github_link}")
    
    for email, subject, name in zip(email_addresses, subjects, names):

        body = email_body_template.format(name=name, RESUME_LINK=resume_link, LINKEDIN_LINK=linkedin_link, GITHUB_LINK=github_link)


        send_email(email, subject, body)

if __name__ == '__main__':
    main()