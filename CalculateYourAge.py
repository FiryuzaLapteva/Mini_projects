import time
from calendar import isleap #True, если год является високосным

# определяем високосный ли год (leap year)
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# возвращаем количество дней в каждом месяце
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
localtime = time.localtime(time.time()) # time.time() - время, выраженное в секундах с начала эпохи,
# по местному времени, передав его функции time.localtime()

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s возраст %d года или " % (name, year), end="")
print("%d месяцев или %d дней" % (month, day))
