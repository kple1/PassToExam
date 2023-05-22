CLanguage = input("C언어 점수를 입력하세요 : ")
if int(CLanguage) >= 90:
    print("Excellence!")
if int(CLanguage) > 100:
    print("점수 입력 범위 (1~100)이 아닙니다")
elif CLanguage == str:
    print("점수 입력시에는 숫자만 입력하세요!")

JavaLanguage = input("자바 점수를 입력하세요 : ")
if int(JavaLanguage) >= 90:
    print("Excellence!")
if int(JavaLanguage) > 100:
    print("점수 입력 범위 (1~100)이 아닙니다")
elif CLanguage == str:
    print("점수 입력시에는 숫자만 입력하세요!")

PythonLanguage = input("파이썬 점수를 입력하세요 : ")
if int(PythonLanguage) >= 90:
    print("Excellence!")
if int(PythonLanguage) > 100:
    print("점수 입력 범위 (1~100)이 아닙니다")
elif CLanguage == str:
    print("점수 입력시에는 숫자만 입력하세요!")

average = int((CLanguage + JavaLanguage + PythonLanguage)) / 3

andThree = JavaLanguage and PythonLanguage and PythonLanguage

if int(andThree) < 60:
    print("과락입니다. 불합격!!")

elif average > 70:
    print("합격입니다.")
