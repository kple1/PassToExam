firstNumber = input("첫 번째 숫자를 입력하세요 : ")

if not firstNumber.isdigit():
    print("숫자만 입력 가능합니다!")

secondNumber = input("두 번째 숫자를 입력하세요 : ")

if not secondNumber.isdigit():
    print("숫자만 입력 가능합니다!")

cacul = input("연산자를 입력하세요(+, -, *, /, %) : ")

if cacul != "+" and cacul != "-" and cacul != "*" and cacul != "/" and cacul != "%":
    print("잘못된 연산자 입니다.")

if cacul == "+":
    resultPlus = int(firstNumber) + int(secondNumber)
    print("두 수의 연산결과는 {}입니다.".format(resultPlus))

if cacul == "-":
    resultMinus = int(firstNumber) - int(secondNumber)
    print("두 수의 연산결과는 {}입니다.".format(resultMinus))

if cacul == "*":
    resultX = int(firstNumber) * int(secondNumber)
    print("두 수의 연산결과는 {}입니다.".format(resultX))

if cacul == "/":
    resultNaN = int(firstNumber) / int(secondNumber)
    print("두 수의 연산결과는 {}입니다.".format(resultNaN))

if cacul == "%":
    resultPer = int(firstNumber) % int(secondNumber)
    print("두 수의 연산결과는 {}입니다.".format(resultPer))
