import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(number, string1):
    if string1 == 'years':
        return starter + datetime.timedelta(days=number*365)
    elif string1 == 'hours':
        return starter + datetime.timedelta(hours=number)
    elif string1 == 'days':
        return starter + datetime.timedelta(days=number)
    elif string1 == 'minutes':
        return starter + datetime.timedelta(minutes=number)
time_machine(3, 'days')