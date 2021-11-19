#!/usr/bin/env python3

from datetime import date
import sys

import sxtwl

LUNAR_MONTHS = [
    '正月', '二月', '三月', '四月', '五月', '六月',
    '七月', '八月', '九月', '十月', '十一月', '腊月'
]
LUNAR_DAYS = [
    '初一', '初二', '初三', '初四', '初五', '初六', '初七', '初八', '初九', '初十',
    '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
    '廿一', '廿二', '廿三', '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十', '卅一'
]


def get_next_solar_birthday(month, day):
    today = date.today()
    year = today.year
    for offset in (0, 1):
        dt = date(year + offset, month, day)
        if dt > today:
            return dt


def get_next_lunar_birthday(month, day):
    today = date.today()
    year = today.year
    for offset in (-1, 0, 1):
        d = sxtwl.fromLunar(year + offset, month, day)
        dt = date(d.getSolarYear(), d.getSolarMonth(), d.getSolarDay())
        if dt > today:
            return dt


def main():
    for birthday in sys.stdin:
        birthday = birthday.strip(' \r\n')
        if not birthday:
            continue

        if '0' <= birthday[0] <= '9':
            m, d = map(int, birthday.split('/'))
            next_birthday = get_next_solar_birthday(m, d)
        else:
            m = LUNAR_MONTHS.index(birthday[:-2]) + 1
            d = LUNAR_DAYS.index(birthday[-2:]) + 1
            next_birthday = get_next_lunar_birthday(m, d)

        # print(birthday)
        print(next_birthday.strftime('%Y-%m-%d'))


if __name__ == '__main__':
    main()
