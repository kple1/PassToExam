import random

print("숫자 맞추기 게임 입니다 1~100")

var0 = 0
var2 = random.randint(1, 100000000)
List = [var2]

while True:
    var0 += 1
    var1 = input("{}번째 시도 : ".format(var0))
    if var1 == "미리보기":
        print(List)

    elif int(var1) > var2:
        print("입력하신 숫자보다 작습니다.")
    elif int(var1) < var2:
        print("입력하신 숫자보다 큽니다.")
    elif int(var1) == var2:
        print("정답입니다.")
        break