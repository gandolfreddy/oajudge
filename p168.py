# notice that the example output is utc+0 time
from datetime import datetime, timezone, timedelta


# input
ts = int(input())

# process
date_ts = datetime.fromtimestamp(ts, tz=timezone.utc)
result = str(date_ts.isoformat(sep=' ')).split('+')[0]

# output
print(result)
