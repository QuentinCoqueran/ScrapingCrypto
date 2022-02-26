import smtplib
import ssl
from email.mime.text import MIMEText
import config


class Mail:
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = config.SERVER_NAME
        self.sender_mail = config.MAIL
        self.password = config.PASSWORD

    def send(self, emails, subject, html_content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{html_content}")

        service.quit()




def send_email(content):
    mails = input("Enter emails: ").split()
    subject = input("Enter subject: ")
    html_content = MIMEText(content, 'html')
    mail = Mail()
    mail.send(mails, subject, html_content)
