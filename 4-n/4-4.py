num = int(input("정수 입력: "))
odd_sum = sum(range(1, num+1, 2))
a = 0
List = []

for i in range(1, num+1, 2):
    List.append(i)
    a += 1
if num % 1 == 0:
    print("1부터 {}까지 숫자 중 홀수 : {}".format(num, List))
    print("1부터 {}까지 숫자 중 홀수의 개수 : {}".format(num, a))
    print("1부터 {}까지 숫자 중 홀수의 합은 {}입니다".format(num, odd_sum))
