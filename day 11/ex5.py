import re
from datetime import datetime

def parse_log_timestamps(log):
    # Regex to match [DD/Mon/YYYY:HH:MM:SS +0000]
    pattern = r"\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]"
    matches = re.findall(pattern, log)

    results = []
    for ts in matches:
        # Parse timestamp string into datetime
        dt = datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S %z")
        # Convert to UTC and reformat
        results.append(dt.astimezone().strftime("%Y-%m-%d %H:%M:%S"))
    
    return results


# Example usage
log_data = """
127.0.0.1 - - [21/Aug/2025:16:20:30 +0000] "GET /index.html HTTP/1.1" 200 123
127.0.0.1 - - [20/Aug/2025:10:05:12 +0000] "POST /login HTTP/1.1" 302 456
"""

print(parse_log_timestamps(log_data))
