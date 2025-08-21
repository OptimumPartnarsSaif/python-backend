import re
from datetime import datetime, timedelta
import pytz

# Sample input string
text = "User: john.doe123@example.com | Date: 2025-08-21 15:30:00"

# Regex patterns
email_pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
date_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"

# Extract email
email_match = re.search(email_pattern, text)
if email_match:
    username, domain = email_match.groups()
    print("✅ Valid Email Found")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("❌ No valid email found")

# Extract date
date_match = re.search(date_pattern, text)
if date_match:
    date_str = date_match.group(1)
    print("\n📅 Date String Found:", date_str)

    # Convert to datetime object
    dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print("Datetime Object:", dt_obj)

    # Format datetime
    formatted = dt_obj.strftime("%d-%b-%Y %I:%M %p")
    print("Formatted Date:", formatted)

    # Add 5 days
    future_date = dt_obj + timedelta(days=5)
    print("Future Date (+5 days):", future_date)

    # Timezone conversion: UTC → Asia/Amman
    utc = pytz.utc
    amman = pytz.timezone("Asia/Amman")

    utc_time = utc.localize(dt_obj)
    amman_time = utc_time.astimezone(amman)
    print("Amman Time:", amman_time)

else:
    print("❌ No valid date found")
