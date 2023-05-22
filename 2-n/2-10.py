a = int(input("국어점수를 입력하시오 : "))
b = int(input("영어점수를 입력하시오 : "))
c = int(input("수학점수를 입력하시오 : "))

result = (a + b + c) / 3
print("당신의 국어, 영어, 수학 성적의 합은 {:.1f}입니다.".format(result))
