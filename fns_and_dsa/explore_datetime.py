# explore_datetime.py

from datetime import datetime, date, timedelta

def display_current_datetime():
    """
    Obtains the current date and time, stores it in 'current_date',
    and prints it in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Get the current date and time
    current_date = datetime.now() # Storing the datetime object in current_date

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date
    based on the current date, and prints it in "YYYY-MM-DD" format.
    """
    try:
        # Prompt the user to enter a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))

        # Get today's date (we only need the date part for this calculation)
        today = date.today()

        # Calculate the future date using timedelta
        # timedelta(days=days_to_add) creates a duration object
        future_date = today + timedelta(days=days_to_add) # Storing the future date

        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")

        # Print the formatted future date
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the datetime exploration tasks.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()


