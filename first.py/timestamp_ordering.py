# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

import datetime

def timestamp_oldest(*argu):
    result = []
    for arg in argu:
        result.append((arg))
        result.sort()
    return datetime.datetime.fromtimestamp(result[0])