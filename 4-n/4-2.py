num = int(input("약수를 구할 정수 입력: "))
print(f"{num}의 약수: ", end="")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
