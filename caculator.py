max = int(input("입력> "))
operator = str(input("연산자> "))
min = int(input("입력> "))

if operator == "+":
    result = max + min
    print(result)
elif operator == "-":
    result = max - min
    print(result)
elif operator == "*":
    result = max * min
    print(result)
elif operator == "/":
    result = max / min
    print(result)
elif operator == "%":
    result = max % min
    print(result)
elif operator == "//":

    result = max // min
    print(result)
