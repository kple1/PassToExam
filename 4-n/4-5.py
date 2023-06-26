startValue = int(input("시작값 : "))
endValue = int(input("마지막값 : "))
addValue = int(input("증가값 : "))

List = []

for i in range(startValue, endValue, addValue):
    List.append(i)
if startValue > addValue:
    print("숫자를 잘못 입력했습니다")
else:
    print("합계를 구할 숫자 들은 {}이며 합계는 {}입니다.".format(List, sum(range(startValue, endValue, addValue))))
