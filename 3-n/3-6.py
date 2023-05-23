CLanguage = input("C언어 점수를 입력하세요 : ")
if not CLanguage.isdigit():
    print("점수 입력시에는 숫자만 입력하세요!")
elif int(CLanguage) >= 90:
    print("Excellence!")
elif int(CLanguage) > 100:
    print("점수 입력 범위 (1~100)이 아닙니다")

JavaLanguage = input("자바 점수를 입력하세요 : ")
if not JavaLanguage.isdigit():
    print("점수 입력시에는 숫자만 입력하세요!")
elif int(JavaLanguage) >= 90:
    print("Excellence!")
elif int(JavaLanguage) > 100:
    print("점수 입력 범위 (1~100)이 아닙니다")

PythonLanguage = input("파이썬 점수를 입력하세요 : ")
if not PythonLanguage.isdigit():
    print("점수 입력시에는 숫자만 입력하세요!")
elif int(PythonLanguage) >= 90:
    print("Excellence!")
elif int(PythonLanguage) > 100:
    print("점수 입력 범위 (1~100)이 아닙니다")

average = (int(CLanguage) + int(JavaLanguage) + int(PythonLanguage)) / 3

andThree = JavaLanguage and PythonLanguage and PythonLanguage

if int(andThree) < 60:
    print("과락입니다. 불합격!!")

if average > 70:
    print("합격입니다.")
else:
    print("불합격")

