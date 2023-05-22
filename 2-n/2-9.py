print("CETI과일가게")
print("1. 사 과 : 800원")
print("2. 바나나 : 2300원")
print("3. 오렌지 : 4700원")
print("")

apple = 800
banana = 2300
orange = 4700

a = int(input("사과를 몇개 구매하시겠습니까? : "))
b = int(input("바나나를 몇개 구매하시겠습니까? : "))
c = int(input("오렌지를 몇개 구매하시겠습니까? : "))

print("당신은 사과" + str(a) + "개")
print("바나나 " + str(b) + "개")
print("오렌지 " + str(c) + "개를 구매해서")

result = a * apple + b * banana + c * orange
print("총 " + str(result) + "원을지불해야 합니다.")

