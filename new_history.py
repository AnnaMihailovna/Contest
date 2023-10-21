from typing import List


def count_days(date: List) -> int:
    """
    Принимает дату и возвращает количество дней,
    прошедших с начала существования ящеров до указанной даты.
    """
    year = date[0]
    month = date[1]
    day = date[2]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(0, month-1):
        days += days_in_month[i]
    days += day
    days += year * 365
    return days

start = list(map(int, input().split()))
end = list(map(int, input().split()))

days_start = count_days(start)
days_end = count_days(end)
delta_days = days_end - days_start

sec_start = start[3] * 3600 + start[4] * 60 + start[5]
sec_end = end[3] * 3600 + end[4] * 60 + end[5]
delta_sec = sec_end - sec_start

if delta_sec < 0:
    delta_days -= 1
    delta_sec+=86400

print(delta_days, delta_sec)
