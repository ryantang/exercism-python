# subclassing the built-in ValueError to create MeetupDayException
from datetime import date
from calendar import monthrange

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

WEEK_RANGE = {
    'teenth': range(13,20),
    'first': range(1,8),
    'second': range(8,15),
    'third': range(15,22),
    'fourth': range(22,29) 
}

def meetup(year, month, week, day_of_week):
    if week == 'last':
        _, last_day_of_month = monthrange(year, month)
        week_range = range(last_day_of_month - 6, last_day_of_month + 1)
        for day in week_range:
            d = date(year, month, day)
            if d.strftime('%A') == day_of_week:
                return d
            
    if week == 'fifth':
        _, last_day_of_month = monthrange(year, month)
        if last_day_of_month < 29:
            raise MeetupDayException('That day does not exist.')
        
        week_range = range(29, last_day_of_month + 1)
        for day in week_range:
            d = date(year, month, day)
            if d.strftime('%A') == day_of_week:
                return d
        
        raise MeetupDayException('That day does not exist.')

        

    for day in WEEK_RANGE[week]:
        d = date(year, month, day)
        if d.strftime('%A') == day_of_week:
            return d
