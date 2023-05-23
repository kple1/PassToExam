leapYear = int(input("연도를 입력하세요: "))

if leapYear % 4 == 0 and leapYear % 400 == 0 and leapYear % 100 == 0:
    print("윤년")

elif leapYear % 4 == 0 and leapYear % 100 == 0:
    print("입력하신 {}년은 400으로 나누어 떨어지지 않고 4와 100으로 나누어 떨어지기 때문에 평년입니다"
          .format(str(leapYear)))

elif leapYear % 4 == 0:
    print("입력하신 {}년은 4로 나누어 떨어지기 때문에 윤년입니다.".format(str(leapYear)))

elif leapYear // 4 != 0:
    print("입력하신 {}년은 4로 나누어 떨어지지 않기 떄문에 평년입니다.".format(str(leapYear)))

