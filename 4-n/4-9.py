googoo = int(input("구구단을 출력할 정수 : "))

for i in range(1, 10, 1):
    print("{} * {} = {}".format(googoo, i, googoo * i))
