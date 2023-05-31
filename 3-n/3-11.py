number = input("정수를 입력하시오 : ")

if not number.isdigit():
    print("슷자만 입력가능합니다.")

elif 3 <= int(number) >= 100:
    print("3~100 사이의 숫자만 입력 가능합니다.!")

elif int(number) % 3 == 0 and int(number) % 5 == 0:
    result2 = int(number) / 3
    result3 = int(number) / 5
    print("입력하신 {}는 {}과 {}의 공배수입니다.".format(number, result2, result3))

elif int(number) % 3 == 0:
    result = int(number) / 3
    print("입력하신 {}는 {}의 배수입니다.".format(number, result))

elif int(number) % 5 == 0:
    result1 = int(number) / 5
    print("입력하신 {}는 {}의 배수입니다.".format(number, result1))
