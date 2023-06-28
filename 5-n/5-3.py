def IsPrime(var1):
    if var1 % 2 != 0:
        print("소수 입니다.")
    else:
        print("소수가 아닙니다.")


var2 = int(input("소수 입력 : "))
IsPrime(var2)
