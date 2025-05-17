from datetime import datetime

def is_business_day(date: datetime) -> bool:
    return date.weekday() < 5  #Monday 0
