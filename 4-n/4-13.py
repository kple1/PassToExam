oneStudent = int(input("1번 학생 점수 입력 : "))
twoStudent = int(input("2번 학생 점수 입력 : "))
threeStudent = int(input("3번 학생 점수 입력 : "))
fourStudent = int(input("4번 학생 점수 입력 : "))
fiveStudent = int(input("5번 학생 점수 입력 : "))

List = [oneStudent, twoStudent, threeStudent, fourStudent, fiveStudent]

for i in List:
    if i >= 80:
        print("{}번 학생의 점수는 {}점 이므로 합격입니다.".format())

