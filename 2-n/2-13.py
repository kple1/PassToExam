a = int(input("물건의 가격을 입력 하시오 : "))
b = int(input("1000짜리 지폐 개수 : "))
c = int(input("500짜리 동전 개수 : "))
d = int(input("100짜리 동전 개수 : "))

operator = b + c + d
if a > operator:
    print("물건 값보다 적은 금액을 투입할 수 없습니다")
    breakpoint()

result = (b * 1000 + c * 500 + d * 100) - a
print("총 거스름 돈은 " + str(result) + "입니다.")
result1 = result // 500
print("거스름 돈 중 500원 짜리는 " + str(result1) + "개 입니다.")
result2 = result % 500 // 100
print("거스름 돈 중 100원 짜리는 " + str(result2) + "개 입니다.")
result3 = result % 100 // 10
print("거스름 돈 중 10원 짜리는 " + str(result3) + "개 입니다.")
result4 = result % 10 // 1
print("거스름 돈 중 1원 짜리는 " + str(result4) + "개 입니다.")
