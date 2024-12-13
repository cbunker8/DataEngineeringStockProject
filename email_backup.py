import smtplib
from email.mime.text import MIMEText

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = ""
app_password = ""
recipient_email = ""

subject = "Test Email"
body = "This is a test email sent using Python smtplib."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")

