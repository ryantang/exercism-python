from datetime import date, time, datetime, timedelta

def delivery_date(start, description):
    dt_format = "%Y-%m-%dT%H:%M:%S"
    meeting_start = datetime.strptime(start, dt_format)
    tomorrow = meeting_start.date() + timedelta(days=1)
    five_pm = time(17, 0)
    one_pm = time(13, 0)
    eight_pm = time(20, 0)

    if description == "NOW":
        datetime_due = meeting_start + timedelta(hours=2)
    elif description == "ASAP" and meeting_start.time() < one_pm:
        datetime_due = datetime.combine(meeting_start.date(), five_pm)
    elif description == "ASAP" and meeting_start.time() >= one_pm:
        datetime_due = datetime.combine(tomorrow, one_pm)
    elif description == "EOW" and meeting_start.weekday in (0, 1, 2):
        days_til_fri = 4 - meeting_start.weekday()
        friday = meeting_start + timedelta(days=days_til_fri)
        datetime_due = datetime.combine(friday.date(), five_pm)
    elif description == "EOW":
        days_til_sun = 6 - meeting_start.weekday()
        sunday = meeting_start + timedelta(days=days_til_sun)
        datetime_due = datetime.combine(sunday.date(), eight_pm)

    return datetime_due.strftime(dt_format)

