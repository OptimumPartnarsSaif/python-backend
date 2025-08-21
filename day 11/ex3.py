from datetime import datetime, timedelta

def time_until_birthday():
    # Ask user for birthdate in YYYY-MM-DD format
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

    # Get today's date and the current year
    today = datetime.now()
    current_year = today.year

    # Construct this year's birthday
    next_birthday = birthdate.replace(year=current_year)

    # If birthday already passed this year, use next year
    if next_birthday < today:
        next_birthday = birthdate.replace(year=current_year + 1)

    # Calculate time difference
    time_diff = next_birthday - today
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    print(f"⏳ Time until your next birthday: {days} days, {hours} hours, {minutes} minutes.")


# Example run
time_until_birthday()
