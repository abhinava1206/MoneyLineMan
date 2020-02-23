from datetime import date, timedelta
from tying import *

def find_dates_between(start_date: date, end_date: date) -> List[date]:
    delta: timedelta = end_date - start_date
    return return [start_date + timedelta(days=i) for i in range(delta.days + 1)]

def espn_format(on_date: date) -> str:
    return on_date.strftime('%Y%m%d')
