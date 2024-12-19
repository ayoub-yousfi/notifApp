from pushbullet import Pushbullet
from datetime import datetime, time as dt_time  # Import 'time' from datetime
import os

# Pushbullet API token (from Pushbullet settings page)
TOKEN_PUSHBULLET = os.getenv("TOKEN_PUSHBULLET")
if not TOKEN_PUSHBULLET:
    raise ValueError("Pushbullet API key not found in environment variables")

# List of Duas
duas = [
    "اللّهُمَّ إِنِّي أَصْبَحْتُ أُشْهِدُكَ وَأُشْهِدُ حَمَلَةَ عَرْشِكَ وَجَمِيعَ خَلْقِكَ أَنَّكَ أَنتَ اللّهُ لَا إِلٰهَ إِلَّا أَنتَ وَحْدَكَ لَا شَرِيكَ لَكَ وَأَنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ",
    "اللهمَّ إنّي أمسيتُ أشهدُكَ وأشهِدُ حملة عرشِك وملائكتِك وجميع خلقك، أنّك أنتَ الله لا إلهَ إلا أنت، وحدك لا شريكَ لك، وأنّ محمداً عبدُك ورسولك",
    "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير، سبحان الله، والحمد لله، ولا إله إلا الله، والله أكبر، ولا حول ولا قوة إلا بالله"
]

# Initialize Pushbullet with the API key
pb = Pushbullet(TOKEN_PUSHBULLET)

# Function to send a daily Dua
def send_daily_dua():
    current_time = datetime.now().time()  # Get current time
    morning_time = dt_time(7, 0)          # 7:00 AM
    midDay_time = dt_time(12, 0)          # 12:00 PM    

    if morning_time <= current_time < midDay_time:
        pb.push_note("Your Daily Dua", duas[0])
    elif midDay_time <= current_time < dt_time(23, 59, 59):  # Before midnight
        pb.push_note("Your Daily Dua", duas[1])
    else:  # Between midnight and morning
        pb.push_note("Your Daily Dua", duas[2])

# Call the function once
send_daily_dua()
