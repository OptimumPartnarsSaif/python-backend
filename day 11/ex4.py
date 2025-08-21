from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):
    # Parse input string into datetime object
    naive_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
    # Attach source timezone
    source_timezone = pytz.timezone(from_tz)
    localized_time = source_timezone.localize(naive_time)
    
    # Convert to target timezone
    target_timezone = pytz.timezone(to_tz)
    converted_time = localized_time.astimezone(target_timezone)
    
    return converted_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")


# Example usage
print(convert_timezone("2023-10-05 14:30:00", "US/Eastern", "UTC"))
print(convert_timezone("2023-10-05 14:30:00", "Asia/Amman", "Europe/London"))
