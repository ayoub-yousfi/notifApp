from pushbullet import Pushbullet
from datetime import datetime
import time
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
    current_time = datetime.now().time() 
    morning_time = time(7, 0)
    midDay_time = time(12, 0)
    midNight_time = time(0, 0)
    if (current_time > morning_time) and (current_time < midDay_time)  :
                pb.push_note("Your Daily Dua", duas[0])
    if (current_time > midDay_time) and (current_time < midNight_time)  :
                pb.push_note("Your Daily Dua", duas[1])
    else :
                pb.push_note("Your Daily Dua", duas[2])
    #dua = duas[int(time.time()) % len(duas)]  # Rotate Duas based on the day

# Call the function once (no infinite loop)
send_daily_dua()
