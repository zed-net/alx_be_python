from datetime import datetime
from datetime import date
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current local date and time (default format):", current_date)
# Example output: Current local date and time (default format): 2025-07-23 18:09:26.123456
display_current_datetime()
num_days = timedelta(days=float(input("Enter the number of days to add to the current date:")))

def calculate_future_date():
    current_date_only = date.today()
    future_date = current_date_only + num_days
    print(future_date)
calculate_future_date()

