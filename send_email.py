import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "testchris###.com"
app_password = "######"
recipient_email = "testchris####"
e_log_path = ""
check_weekend_log_path = ""

try:
    with open(e_log_path, "r") as e_log_file:
        e_log_content = e_log_file.read()
except FileNotFoundError:
    e_log_content = "e.log not found."

try:
    with open(check_weekend_log_path, "r") as check_weekend_log_file:
        check_weekend_log_content = check_weekend_log_file.read()
except FileNotFoundError:
    check_weekend_log_content = "check_weekend.log not found."

subject = "Cron Job Logs"
body = (
    "Here are the latest logs from the cron jobs:\n\n"
    "=== e.log ===\n"
    f"{e_log_content}\n\n"
    "=== check_weekend.log ===\n"
    f"{check_weekend_log_content}"
)

msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email

msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully with logs!")
except Exception as e:
    print(f"Error sending email: {e}")
