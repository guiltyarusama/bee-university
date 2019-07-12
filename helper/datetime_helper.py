import logging
from datetime import datetime

import pytz

logger = logging.getLogger(__name__)


def get_datetime_from_timestamp(timestamp):
    # logger.info('get_datetime_from_timestamp', timestamp)
    """
    Get date time from timestamp by milisecond or second unit
    :param timestamp: timestamp by milisecond or second unit
    :return: datetime
    """
    if timestamp is None:
        return None
    try:
        timestamp = int(timestamp)
        if len(str(timestamp)) < 13:
            return datetime.fromtimestamp(timestamp)
        else:
            return datetime.fromtimestamp(int(timestamp / 1000))
    except Exception as e:
        logger.warning(e)


def get_datetime_tz_from_timestamp(timestamp, timezone='Asia/Ho_Chi_Minh'):
    d = get_datetime_from_timestamp(timestamp)

    if d is None:
        return None
    # timezone = pytz.timezone(settings.TIME_ZONE)
    timezone = pytz.timezone(timezone)
    datetime_with_timezone = timezone.localize(d)
    # print(datetime_with_timezone)
    return datetime_with_timezone


def get_timestamp_now(should_timestamp_second=True):
    if should_timestamp_second:
        return int(datetime.now().timestamp())
    return int(datetime.now().timestamp())


def get_date_time_now_with_timezone(timezone='Asia/Ho_Chi_Minh'):
    return get_datetime_tz_from_timestamp(get_timestamp_now(), timezone)


def get_str_iso_time_from_timestamp(timestamp, timezone='Asia/Ho_Chi_Minh'):
    # ts = os.path.getctime(timestamp)
    dt = datetime.fromtimestamp(timestamp, pytz.timezone(timezone))
    return dt.isoformat()


def convert_str_to_datetime(str, format='%Y-%m-%d %H:%M:%S'):
    if str is not None and len(str) > 0:
        return datetime.strptime(str, format)
    return None


def get_date_current():
    date_current = datetime.now().strftime("%Y%m%d")
    # print(date_current)
    return date_current


def get_date_time_current():
    date_time_current = datetime.now().strftime("%Y%m%d_%H")
    # print(date_time_current )
    return date_time_current


# print(get_datetime_from_timestamp(1557644420))
# print(get_str_iso_time_from_timestamp(1557644420))
if __name__ == '__main__':
    str = '2018-12-04 17:16:58'
    print(convert_str_to_datetime(str).timestamp())
