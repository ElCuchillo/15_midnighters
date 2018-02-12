import requests
import pytz
from datetime import datetime, date, time, timedelta
from itertools import groupby


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts'
    page, number_of_pages = 1, 1
    while page <= number_of_pages:
        pay_load = {'page': page}
        json_data = requests.get(url, params=pay_load).json()
        for attempt in json_data['records']:
            yield {
                'username': attempt['username'],
                'timestamp': attempt['timestamp'],
                'timezone': attempt['timezone'],
            }
        number_of_pages = int(json_data['number_of_pages'])
        page += 1


def get_local_time(timestamp, tz):
    timezone = pytz.timezone(tz)
    return datetime.fromtimestamp(timestamp, tz=timezone)


def is_midnight(attempt, night_hours):
    attempt_time = get_local_time(attempt['timestamp'], attempt['timezone'])
    return attempt_time.hour < night_hours


def get_midnighters(attempts_list, night_hours):
    night_owls = [(
        attempt['username'],
        attempt['timestamp'],
        attempt['timezone']
        )
        for attempt in attempts_list if is_midnight(attempt, night_hours)
    ]
    return night_owls


def print_midnighters(night_owls, night_hours):
    print("DEVMAN's Night Owls, who made their attmepts "
          "since 24:00 till {}:00 are:".format(night_hours))
    night_owls.sort(key=lambda x: x[0])
    for user, attempt in groupby(night_owls, lambda x: x[0]):
        print('\n{}:'.format(user))
        for name, time, tz in attempt:
            user_time = get_local_time(time, tz)
            print('   {}'.
                format(user_time.strftime('%Y/%m/%d %H:%M %Z%z')))


if __name__ == '__main__':
    night_hours = 6
    attempts_list = list(load_attempts())
    night_owls = get_midnighters(attempts_list, night_hours)
    print_midnighters(night_owls, night_hours)
