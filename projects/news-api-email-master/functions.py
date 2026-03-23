from datetime import date, timedelta


def get_prev_month_date():
    # Get today's date
    today = date.today()
    # Calculate the date of the first day of the previous month
    first_day_of_prev_month = date(today.year, today.month - 1, 1)
    # Calculate the date of the last day of the previous month
    last_day_of_prev_month = first_day_of_prev_month.replace(day=28) + timedelta(days=4)
    last_day_of_prev_month = last_day_of_prev_month.replace(day=1) - timedelta(days=1)
    # Format the date string in the desired format
    prev_month_str = last_day_of_prev_month.strftime("%Y-%m-%d")

    return prev_month_str