import datetime


def print_zodiac(name, age, year):
    print("{}님의 나이는 {}살이고 {} 띠입니다.".format(name, age, year))


name = input("이름: ")
nowYear = datetime.datetime.now()
var1 = int(input("태어난 년도: "))
age = nowYear.year - var1

year = var1 % 12
List = ["신", "유", "술", "해", "자", "축", "인", "묘", "진", "사", "오", "미"]

for i in List:
    if i is year:
        print_zodiac(name, age, year)
