num = int(input("정수: "))
digit_sum = 0
# 입력된 정수를 문자열로 변환하여 각 자릿수를 합산 ㄹㅇ천재 발상
for digit in str(num):
    digit_sum += int(digit)

print("자릿수의 합:", digit_sum)
