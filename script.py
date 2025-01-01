import requests
import os

# Your Brevo API key
BREVO_KEY = os.getenv("BREVO_KEY")
if not BREVO_KEY:
    raise ValueError("Brevo API key not found in environment variables")
# API endpoint for sending transactional emails
url = "https://api.brevo.com/v3/smtp/email"

# Payload with email details
payload = {
    "sender": {"name": "Your Name", "email": "ayoub.yousfi.enetcom@gmail.com"},
    "to": [{"email": "ayoub.yousfi.enetcom@gmail.com", "name": "Recipient Name"}],
    "subject": "Test Email from Brevo API",
    "htmlContent": "<p>This is a test email sent via Brevo API.</p>"
}

# Headers for API request
headers = {
    "accept": "application/json",
    "api-key": BREVO_KEY,
    "content-type": "application/json"
}

# Sending the request
response = requests.post(url, json=payload, headers=headers)

# Printing the response
if response.status_code == 201:
    print("Email sent successfully!")
else:
    print(f"Failed to send email: {response.status_code}, {response.text}")
