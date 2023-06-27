print("숫자 맞추기 게임입니다 1~100")
var0 = 0

while True:
    var0 += 1
    var1 = int(input("{}번째 시도 : ".format(var0)))
    if var1 > 14:
        print("입력하신 숫자보다 작습니다.")
    elif var1 < 14:
        print("입력하신 숫자보다 큽니다.")
    else:
        print("정답입니다.")
        break
