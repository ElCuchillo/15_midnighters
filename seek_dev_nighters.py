import requests
import pytz
from datetime import datetime, date, time, timedelta


def load_attempts(pages=10):
    url = 'https://devman.org/api/challenges/solution_attempts'
    for page in range(1, pages):
        pay_load = {'page': page}
        response = requests.get(url, params=pay_load).json()['records']
        for item in response:
            yield {
                'username': item['username'],
                'timestamp': item['timestamp'],
                'timezone': item['timezone'],
            }


def midnight_test(attempt, night_hours):
    timezone = pytz.timezone(attempt['timezone'])
    attempt_time = pytz.utc.localize(
        datetime.utcfromtimestamp(attempt['timestamp'])).\
        astimezone(timezone)
    midnight = timezone.localize(
        datetime.combine(attempt_time.date(), time(0, 0)))
    morning = midnight + timedelta(hours=night_hours)
    return (attempt_time > midnight) and (attempt_time <= morning)


def get_midnighters(attempts_list, night_hours):
    midnighters_list = [attempt for attempt in attempts_list
        if midnight_test(attempt, night_hours)]
    return midnighters_list


def print_midnighters(midnighters_list, night_hours):
    print("DEVMAN's Night Owls, who made their attmepts "
          "since 24:00 till {}:00 are:\n".format(night_hours))
    for user in midnighters_list:
        timezone = pytz.timezone(user['timezone'])
        user_time = pytz.utc.localize(
            datetime.utcfromtimestamp(user['timestamp'])).astimezone(timezone)
        print('{} at {}, timezone {}'.format(user['username'],
            user_time.strftime('%Y-%m-%d %H:%M %Z%z'), user['timezone']))


if __name__ == '__main__':
    night_hours = 6
    attempts_list = load_attempts()
    midnighters_list = get_midnighters(attempts_list, night_hours)
    print_midnighters(midnighters_list, night_hours)
    
