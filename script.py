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
    "sender": {"name": "Dua", "email": "ayoub.yousfi.enetcom@gmail.com"},
    "to": [{"email": "ayoub.yousfi.enetcom@gmail.com", "name": "Ayoub"}],
    "subject": "Morning Dua",
    "htmlContent": "اللّهُمَّ إِنِّي أَصْبَحْتُ أُشْهِدُكَ وَأُشْهِدُ حَمَلَةَ عَرْشِكَ وَجَمِيعَ خَلْقِكَ أَنَّكَ أَنتَ اللّهُ لَا إِلٰهَ إِلَّا أَنتَ وَحْدَكَ لَا شَرِيكَ لَكَ وَأَنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ"
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
