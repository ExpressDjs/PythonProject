import smtplib, ssl
import UsernamePassword AS UP

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = UP.sender_email
receiver_email = UP.receiver_email
password = UP.password
message = """\
Subject: Motion Found

There has been montion on the camera"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

exit()
