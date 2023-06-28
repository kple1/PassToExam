def gugudan(var):
    for i in range(1, 9 + 1, 1):
        print("{} * {} = {}".format(var, str(i), str(7 * i)))


var = int(input("구구단을 출력할 정수 : "))
gugudan(var)

