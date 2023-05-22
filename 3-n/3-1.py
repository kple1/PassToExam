a = input("주민번호 7자리를 입력 하시오> ")

if not a[6] == int:
    print("마지막 입력문자가 숫자가 아닙니다.")

elif int(a) > 10000000:
    print("문자열 입력길이 초과")

elif int(a[6]) >= 7:
    print("유효한 번위의 숫자가 아닙니다")

elif int(a) >= 100000:
    if int(a) % 2 == 1:
        print("당신은 남성 입니다")
    else:
        print("당신은 여성 입니다")
