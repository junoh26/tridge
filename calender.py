# Question 1
from datetime import date


def numSundaysOnFirstOfMonth(start, end):
    numSundays = 0
    for year in range(start, end+1):
        for month in range(1, 13):
            # weekday() returns Sunday as int 6
            if date(year, month, 1).weekday() == 6:
                numSundays += 1
    return numSundays

if __name__ == '__main__':
    print(numSundaysOnFirstOfMonth(1901,2000))
    