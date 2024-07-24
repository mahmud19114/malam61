class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # Carry over seconds if it exceeds 59
    if sum.second >= 60:
        extra_minutes = sum.second // 60
        sum.second %= 60
        sum.minute += extra_minutes
    
    # Carry over minutes if it exceeds 59
    if sum.minute >= 60:
        extra_hours = sum.minute // 60
        sum.minute %= 60
        sum.hour += extra_hours
    
    return sum
