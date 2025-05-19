import random
import smtplib
from email.mime.text import MIMEText

# Step 1: Configuration (Edit these before running)
sender_email = "youremail@gmail.com"          # Replace with your email
sender_password = "yourapppassword"           # Use an App Password if using Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Step 2: Get recipient email
recipient_email = input("Enter your email address for verification: ")

# Step 3: Generate random 4-digit code
verification_code = str(random.randint(1000, 9999))

# Step 4: Compose the email
subject = "Your Verification Code"
body = f"Your 2FA code is: {verification_code}"
message = MIMEText(body)
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# Step 5: Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Verification code sent to your email.")
except Exception as e:
    print("Failed to send email:", e)
    exit()

# Step 6: Prompt user to enter the code
user_input = input("Enter the 4-digit verification code: ")

# Step 7: Validate code
if user_input == verification_code:
    print("2FA verification successful.")
else:
    print("Incorrect code. Access denied.")
