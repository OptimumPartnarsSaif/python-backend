import re
from datetime import datetime
import pytz

# Function to validate email
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Sample emails
emails = [
    "john.doe@example.com",
    "invalid-email@.com",
    "alice123@gmail.com",
    "bob_at_yahoo.com"
]

print("📧 Email Validation Results:")
for email in emails:
    if validate_email(email):
        print(f"✅ {email} is valid")
    else:
        print(f"❌ {email} is invalid")

print("\n🕒 Current Time in Different Timezones:")

# Timezones to display
timezones = ["UTC", "Asia/Amman", "America/New_York", "Europe/London", "Asia/Tokyo"]

for tz in timezones:
    zone = pytz.timezone(tz)
    now = datetime.now(zone)
    print(f"{tz}: {now.strftime('%Y-%m-%d %H:%M:%S')}")
