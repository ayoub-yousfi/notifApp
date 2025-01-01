import requests
import os
from datetime import datetime, time as dt_time  # Import 'time' from datetime

# Your Brevo API key
BREVO_KEY = os.getenv("BREVO_KEY")
if not BREVO_KEY:
    raise ValueError("Brevo API key not found in environment variables")
# API endpoint for sending transactional emails
url = "https://api.brevo.com/v3/smtp/email"

current_time = datetime.now().time()  # Get current time
morning_time = dt_time(7, 0)          # 7:00 AM
midDay_time = dt_time(12, 0)          # 12:00 PM    
if morning_time <= current_time < midDay_time:
    dua = "اللّهُمَّ إِنِّي أَصْبَحْتُ أُشْهِدُكَ وَأُشْهِدُ حَمَلَةَ عَرْشِكَ وَجَمِيعَ خَلْقِكَ أَنَّكَ أَنتَ اللّهُ لَا إِلٰهَ إِلَّا أَنتَ وَحْدَكَ لَا شَرِيكَ لَكَ وَأَنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ"
    duaTime = "Morning Dua"
elif midDay_time <= current_time < dt_time(23, 59, 59):  # Before midnight
    dua = "اللهمَّ إنّي أمسيتُ أشهدُكَ وأشهِدُ حملة عرشِك وملائكتِك وجميع خلقك، أنّك أنتَ الله لا إلهَ إلا أنت، وحدك لا شريكَ لك، وأنّ محمداً عبدُك ورسولك"
    duaTime = "Midday Dua"
else:  # Between midnight and morning
    dua = "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير، سبحان الله، والحمد لله، ولا إله إلا الله، والله أكبر، ولا حول ولا قوة إلا بالله"
    duaTime = "Midnight Dua"

# Payload with email details
payload = {
    "sender": {"name": "Dua", "email": "ayoub.yousfi.enetcom@gmail.com"},
    "to": [{"email": "ayoub.yousfi.enetcom@gmail.com", "name": "Ayoub"}],
    "subject": duaTime,
    "htmlContent": dua
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
