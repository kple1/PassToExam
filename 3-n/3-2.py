a = int(input("탑승자의 나이를 입력하세요 : "))
b = float(input("탑승자의 키를 입력하세요 : "))

age = 8 - a
key = 140 - b

if (a < 8):
    print("당신은 나이가 {}세 부족해서 탑승이 불가능합니다".format(age))

if (b < 140):
    print("당신은 키가 {:.1f}cm 부족해서 탑승이 불가능합니다.".format(key))
