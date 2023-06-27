var1 = int(input("몇 개의 요소를 리스트에 넣으시겠습니까? : "))

var2 = []

for i in range(1, var1 + 1, 1):
    var3 = int(input("{}번째 요소 입력 : ".format(str(i))))
    var2.append(var3)
print("리스트의 최댓값은 {}이고 최솟값은 {}입니다.".format(max(var2), min(var2)))
print(var2)
