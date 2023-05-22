car = input("운전면허 종류를 입력하세요(1종 또는 2종) : ")
point = int(input("점수를 입력하세요 : "))

result_a = 70 - point
result_b = 60 - point

if not car == "1종" and "2종":
    print("잘못된 운전면허 종류를 입력했습니다!")

if car == "1종":
    if point >= 70:
        print("합격")
    else:
        print("불합격입니다. {}점이 부족하네요 ㅜㅜ".format(result_a))

if car == "2종":
    if point >= 60:
        print("합격")
    else:
        print("불합격입니다. {}점이 부족하네요 ㅜㅜ".format(result_b))
