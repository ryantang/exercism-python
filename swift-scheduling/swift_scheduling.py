from datetime import date, time, datetime, timedelta
import re
import calendar

# Q1: March, Q2: June, etc.
QUARTER_LAST_MONTH_MAPPING = {
    1: 3,
    2: 6,
    3: 9,
    4: 12,
}

EIGHT_AM = time(8, 0)
ONE_PM = time(13, 0)
FIVE_PM = time(17, 0)
EIGHT_PM = time(20, 0)

WEDNESDAY = 2
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"


def _handle_eow(meeting_start: datetime) -> datetime:
    """Calculate the end-of-week due date."""
    if meeting_start.weekday() <= WEDNESDAY:
        day_of_week_due, time_due = FRIDAY, FIVE_PM
    else:
        day_of_week_due, time_due = SUNDAY, EIGHT_PM

    days_til_due = day_of_week_due - meeting_start.weekday()
    date_due = meeting_start + timedelta(days=days_til_due)
    return datetime.combine(date_due.date(), time_due)

def _handle_asap(meeting_start: datetime) -> datetime:
    """Calculate the 'as soon as possible' due date."""
    if meeting_start.time() < ONE_PM:
        return datetime.combine(meeting_start.date(), FIVE_PM)

    return datetime.combine(meeting_start.date() + timedelta(days=1), ONE_PM)

def _handle_now(meeting_start: datetime) -> datetime:
    """Calculate the 'now' due date (2 hours from start)."""
    return meeting_start + timedelta(hours=2)



HANDLERS = {
    "NOW": _handle_now,
    "ASAP": _handle_asap,
    "EOW": _handle_eow,
}

def delivery_date(start: str, description: str) -> str:
    """Calculate the delivery date based on a start date and description.

    :param start: A string representing the start datetime in ISO format.
    :param description: A string code describing the delivery urgency.
    :return: A string representing the calculated due datetime in ISO format.
    """
    meeting_start = datetime.strptime(start, DATETIME_FORMAT)

    month_match = re.search(r"(\d+)M", description)
    if month_match:
        datetime_due = _first_workday_of_month(meeting_start, int(month_match.group(1)))
        return datetime_due.strftime(DATETIME_FORMAT)

    quarter_match = re.search(r"Q(\d)", description)
    if quarter_match:
        datetime_due = _last_workday_of_quarter(meeting_start, int(quarter_match.group(1)))
        return datetime_due.strftime(DATETIME_FORMAT)

    func = HANDLERS.get(description)
    if not func:
        raise ValueError("Description doesn't match boss' code")
    datetime_due = func(meeting_start)
    return datetime_due.strftime(DATETIME_FORMAT)


def _first_workday_of_month(meeting_start: datetime, month: int) -> datetime:
    """Calculate the first workday of a given month."""
    if meeting_start.month < month:
        year = meeting_start.year
    else:
        year = meeting_start.year + 1

    first_of_month = date(year, month, 1)

    days_til_workday = 0
    if first_of_month.weekday() == SATURDAY:
        days_til_workday = 2
    elif first_of_month.weekday() == SUNDAY:
        days_til_workday = 1

    return datetime.combine(first_of_month + timedelta(days=days_til_workday) , EIGHT_AM)

def _last_workday_of_quarter(meeting_start: datetime, quarter_due: int) -> datetime:
    """Calculate the last workday of a given quarter."""
    month_due = QUARTER_LAST_MONTH_MAPPING[quarter_due]

    current_quarter = (meeting_start.month - 1)//3 + 1
    if current_quarter > quarter_due:
        year = meeting_start.year + 1
    else:
        year = meeting_start.year

    _, day_of_month = calendar.monthrange(year, month_due)
    last_of_month = date(year, month_due, day_of_month)

    days_past_last_workday = 0
    if last_of_month.weekday() == SATURDAY:
        days_past_last_workday = 1
    elif last_of_month.weekday() == SUNDAY:
        days_past_last_workday = 2

    return datetime.combine(last_of_month - timedelta(days=days_past_last_workday), EIGHT_AM)
