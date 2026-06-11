"""Small script to return the date that fits the description or throws a custom error"""
# subclassing the built-in ValueError to create MeetupDayException
from datetime import date
from calendar import monthrange

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

WEEK_RANGE = {
    'teenth': range(13, 20),
    'first': range(1, 8),
    'second': range(8, 15),
    'third': range(15, 22),
    'fourth': range(22, 29) 
}

def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    """Returns the date that fits the meetup day description"""
    _, last_of_month = monthrange(year, month)
    if week == 'fifth' and last_of_month < 29:
        raise MeetupDayException('That day does not exist.')

    if week == 'last':
        week_range = range(last_of_month - 6, last_of_month + 1)
    elif week == 'fifth':
        week_range = range(29, last_of_month + 1)
    else:
        week_range = WEEK_RANGE[week]

    for day in week_range:
        candidate = date(year, month, day)
        if candidate.strftime('%A') == day_of_week:
            return candidate

    raise MeetupDayException('That day does not exist.')
