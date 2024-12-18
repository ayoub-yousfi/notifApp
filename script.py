from pushbullet import Pushbullet
import time

# Pushbullet API token (from Pushbullet settings page)
API_KEY = "wwwwww"

# List of Duas
duas = [
    "اللّهُمَّ اجْعَلْنِي مِنَ المُتَّقِينَ",
    "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً",
    "اللَّهُمَّ ارْزُقْنِي رِزْقًا حَلَالًا طَيِّبًا",
]

# Initialize Pushbullet with the API key
pb = Pushbullet(API_KEY)

# Function to send a daily Dua
def send_daily_dua():
    dua = duas[int(time.time()) % len(duas)]  # Rotate Duas based on the day
    pb.push_note("Your Daily Dua", dua)  # Send the Dua as a notification to your phone
    print("Dua sent to Pushbullet!")

# Call the function daily
while True:
    send_daily_dua()
    time.sleep(86400)  # Wait for 24 hours before sending again
