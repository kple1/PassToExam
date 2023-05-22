age = input("나이를 입력하세요 : ")

if not age.isdigit():
    print("숫자가 아닙니다.")

elif int(age) > 8 or int(age) > 65:
    print("버스요금은 무료입니다.")

elif 8 > int(age) > 19:
    print("버스 요금은 1000원")

elif 20 > int(age) > 64:
    print("버스 요금은 1500원")
