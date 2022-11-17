PERIOD_OPPOSITES = {"AM": "PM", "PM": "AM"}
DAYS_OF_WEEK = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}


def clock_variables(start: str) -> (int, int):
    clock_time, period = start.split()
    clock_hour, clock_minutes = clock_time.split(':')
    return int(clock_hour), int(clock_minutes), period


def duration_variables(duration: str) -> (int, int):
    duration_hour, duration_minutes = duration.split(':')
    return int(duration_hour), int(duration_minutes)


def to_new_minutes(actual_minutes: int, addition_minutes: int, actual_hour: int) -> (int, int):
    new_minutes = actual_minutes + addition_minutes
    if new_minutes > 60:
        new_minutes %= 60
        actual_hour += 1
    return actual_hour, new_minutes


def to_new_hour(actual_hour: int, addition_hour: int) -> int:
    new_hour = (actual_hour + addition_hour) % 12
    return new_hour


def am_or_pm(actual_hour: int, addition_hour: int, period: str) -> str:
    period_flips = (actual_hour + addition_hour) // 12
    return PERIOD_OPPOSITES[period] if period_flips % 2 == 1 else period


def days_passed_quantity(addition_hour: int, period: str, actual_hour: int) -> int:
    days_passed = addition_hour // 24
    if period == "PM" and actual_hour + (addition_hour % 12) >= 12:
        days_passed += 1
    return days_passed


def to_new_day(day: int, days_passed: int) -> str:
    new_day = DAYS_OF_WEEK.get(int(DAYS_OF_WEEK[day] + days_passed) % 7)
    return new_day


def formatted_time(hour: int, minutes: int, days_later: int, period: str, day: str = "") -> str:
    hour = 12 if hour == 0 else hour
    minutes = minutes if minutes > 9 else "0" + str(minutes)
    if not days_later and not day:
        return f"{hour}:{minutes} {period}"
    if not day:
        return f"{hour}:{minutes} {period} (" \
               f"{str(days_later) + ' days later)' if days_later > 1 else 'next day)'}"
    if not days_later:
        return f"{hour}:{minutes} {period}, {day}"
    return f"{hour}:{minutes} {period}, {day} (" \
           f"{str(days_later) + ' days later)' if days_later > 1 else 'next day)'}"


def add_time(start: str, duration: str, day: str = "") -> str:
    day = day.capitalize()
    start_hour, start_minutes, start_period = clock_variables(start)
    duration_hour, duration_minutes = duration_variables(duration)
    actual_hour, actual_minutes = to_new_minutes(start_minutes, duration_minutes, start_hour)
    actual_period = am_or_pm(actual_hour, duration_hour, start_period)
    days_later = days_passed_quantity(duration_hour, start_period, actual_hour)
    actual_hour = to_new_hour(actual_hour, duration_hour)
    if not day:
        return formatted_time(actual_hour, actual_minutes, days_later, actual_period, day)
    actual_day = to_new_day(day, days_later)
    return formatted_time(actual_hour, actual_minutes, days_later, actual_period, actual_day)


if __name__ == "__main__":
    print(add_time("11:40 AM", "0:25"))
    print(add_time("11:55 AM", "3:07"))
    print(add_time("11:59 PM", "24:05"))
    print(add_time("2:59 AM", "24:00", "saturDay"))
