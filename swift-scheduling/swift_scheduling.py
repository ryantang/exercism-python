from datetime import date, time, datetime, timedelta
import re
import calendar

def delivery_date(start, description):
    dt_format = "%Y-%m-%dT%H:%M:%S"
    meeting_start = datetime.strptime(start, dt_format)
    tomorrow = meeting_start.date() + timedelta(days=1)
    five_pm = time(17, 0)
    one_pm = time(13, 0)
    eight_pm = time(20, 0)
    # eight_am = time(8, 0)

    month_match = re.search(r"(\d+)M", description)
    quarter_match = re.search(r"Q(\d)", description)

    if description == "NOW":
        datetime_due = meeting_start + timedelta(hours=2)
    elif description == "ASAP" and meeting_start.time() < one_pm:
        datetime_due = datetime.combine(meeting_start.date(), five_pm)
    elif description == "ASAP" and meeting_start.time() >= one_pm:
        datetime_due = datetime.combine(tomorrow, one_pm)
    elif description == "EOW" and meeting_start.weekday() in (0, 1, 2):
        days_til_fri = 4 - meeting_start.weekday()
        friday = meeting_start + timedelta(days=days_til_fri)
        datetime_due = datetime.combine(friday.date(), five_pm)
    elif description == "EOW":
        days_til_sun = 6 - meeting_start.weekday()
        sunday = meeting_start + timedelta(days=days_til_sun)
        datetime_due = datetime.combine(sunday.date(), eight_pm)
    elif month_match:
        print(f"scheduling for the last day of month {month_match.group(1)}")
        datetime_due = _first_workday(meeting_start, int(month_match.group(1)))
    elif quarter_match:
        print(f"scheduling for the last day of month {quarter_match.group(1)}")
        datetime_due = _last_workday(meeting_start, int(quarter_match.group(1)))


    return datetime_due.strftime(dt_format)

def _first_workday(meeting_start, month):
    if meeting_start.month < month:
        year = meeting_start.year
    else:
        year = meeting_start.year + 1
    
    first_of_month = date(year, month, 1)
    
    if first_of_month.weekday() < 5: # Mon - Fri
        first_workday = first_of_month
    elif first_of_month.weekday() == 5: # Sat
        first_workday = date(year, month, 3)
    else: # Sun
        first_workday = date(year, month, 2)
    
    return datetime.combine(first_workday, time(8, 0))

def _last_workday(meeting_start, quarter_due):
    quarter_month_mapping = {1: 3, 2: 6, 3: 9, 4: 12}
    month_due = quarter_month_mapping[quarter_due]

    current_quarter = (meeting_start.month - 1)//3 + 1
    if current_quarter > quarter_due:
        year = meeting_start.year + 1
    else:
        year = meeting_start.year

    _, day_of_month = calendar.monthrange(year, month_due)
    last_of_month = date(year, month_due, day_of_month)
    if last_of_month.weekday() < 5: # Mon - Fri
        last_day = date(year, month_due, day_of_month)
    elif last_of_month.weekday() == 5: # Sat
        last_day = date(year, month_due, day_of_month - 1)
    else: # Sun
        last_day = date(year, month_due, day_of_month - 2)

    return datetime.combine(last_day, time(8, 0))
