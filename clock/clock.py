class Clock:
    """A clock that handles hours and minutes with automatic normalization."""

    def __init__(self, hour: int, minute: int) -> None:
        """Initialize a clock with the given hour and minute.
        
        Automatically normalizes minutes to hours and wraps hours to 24-hour format.
        """
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        """Return a developer-friendly string representation."""
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self) -> str:
        """Return a formatted time string in HH:MM format."""
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other: object) -> bool:
        """Check equality between two Clock instances."""
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> 'Clock':
        """Add minutes to the clock, returning a new Clock instance."""
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> 'Clock':
        """Subtract minutes from the clock, returning a new Clock instance."""
        return Clock(self.hour, self.minute - minutes)
