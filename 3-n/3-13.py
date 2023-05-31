print("세 변의 길이를 입력받습니다 \n"
      "가장 긴 변이 나머지 두 변의 길이의 합보다 길다면 삼각형은 성립되지 않습니다")

first = int(input("첫 번째 변의 길이 : "))
second = int(input("두 번째 변의 길이 : "))
third = int(input("세 번째 변의 길이 : "))

if first > (second + third):
    print("삼각형이 성립되지 않습니다")

elif second > (first + third):
    print("삼각형이 성립되지 않습니다")

elif third > (first + second):
    print("삼각형이 성립되지 않습니다")

elif first < (second + third):
    print("삼각형이 성립됩니다")

elif second < (first + third):
    print("삼각형이 성립됩니다")

elif third < (first + second):
    print("삼각형이 성립됩니다")

