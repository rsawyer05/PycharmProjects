import datetime

def minutes(dt1, dt2):
    dt3 = dt2 - dt1
    return round(dt3.total_seconds() / 60)