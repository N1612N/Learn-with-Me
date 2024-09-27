def is_leap(year):
    leap = False

    if year % 4 != 0:
        leap = False
    if year % 4 == 0:
        if year // 100 % 2 == 0:
            leap = False
        elif year // 400 % 2 == 0:
            leap = True

    return leap

year = int(input())
print(is_leap(year))