from datetime import timedelta, datetime
from typing import List, Tuple


def date_range(start, stop) -> List[Tuple[str, str]]:

    dates = []
    diff = (stop - start).days
    for i in range(diff + 1):
        day = start + timedelta(days=i)
        day = datetime.combine(day, datetime.min.time())
        dates.append(day)

    if not dates:
        raise

    dates = convert_datetime_to_timestamp(dates)
    dates = batch_dates(dates)

    return dates


def convert_datetime_to_timestamp(dates: List[datetime]) -> List[str]:

    timestampdate = []
    for date in dates:
        timestampdate.append(str(int(datetime.timestamp(date))))

    return timestampdate


def batch_dates(dates: List[str]) -> List[Tuple[str, str]]:

    start_list = 0
    # next_end_list = 6
    next_end_list = len(dates) - 1

    list_date_batch = []

    while dates:

        try:
            start_date = dates[start_list]
        except IndexError:
            break

        try:
            end_date = dates[next_end_list]
        except IndexError:
            end_date = dates[len(dates) - 1]
            next_end_list = len(dates)

        list_date_batch.append((start_date, end_date))

        del dates[0 : next_end_list + 1]

    return list_date_batch
