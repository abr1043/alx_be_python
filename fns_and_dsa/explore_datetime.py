from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # return for reuse

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")
    return future_date

def main():
    current_date = display_current_datetime()

    user_input = input("Enter the number of days to add to the current date: ").strip()
    try:
        days = int(user_input)
    except ValueError:
        print("Invalid number of days. Please enter an integer.")
        return

    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
