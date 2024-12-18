from pushbullet import Pushbullet
import time
import os

# Pushbullet API token (from Pushbullet settings page)
TOKEN_PUSHBULLET = os.getenv("TOKEN_PUSHBULLET")
if not TOKEN_PUSHBULLET:
    raise ValueError("Pushbullet API key not found in environment variables")

# List of Duas
duas = [
    "اللّهُمَّ اجْعَلْنِي مِنَ المُتَّقِينَ",
    "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً",
    "اللَّهُمَّ ارْزُقْنِي رِزْقًا حَلَالًا طَيِّبًا",
]

# Initialize Pushbullet with the API key
pb = Pushbullet(TOKEN_PUSHBULLET)

# Function to send a daily Dua
def send_daily_dua():
    dua = duas[int(time.time()) % len(duas)]  # Rotate Duas based on the day
    pb.push_note("Your Daily Dua", dua)  # Send the Dua as a notification to your phone
    print("Dua sent to Pushbullet!")

# Call the function once (no infinite loop)
send_daily_dua()
