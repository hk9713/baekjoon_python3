# 윤년 판별
year = int(input())
if (year % 4 == 0) & (year % 100 != 0 ) | (year % 400 == 0) :
    print(1)
else:
    print(0)