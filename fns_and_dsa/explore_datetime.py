from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days):
    """
    Calculate the future date after adding a specified number of days to the current date.

    Parameters:
    current_date (datetime): The current date and time.
    days (int): The number of days to add.

    Returns:
    datetime: The future date.
    """
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date (after {days} days): {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
