import smtplib, ssl
from dotenv import load_dotenv
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    load_dotenv()
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("EMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
