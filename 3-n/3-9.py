one = input("첫 번째 숫자를 입력하세요 : ")
two = input("두 번째 숫자를 입력하세요 : ")
three = input("세 번째 숫자를 입력하세요 : ")

if not one.isdigit() and two.isdigit() and three.isdigit():
    print("숫자만 입력 가능합니다!")

if one > two and two > three:
    print("세 개의 정수중 최댓값은 {}입니다.".format(one))
if two > one and two > three:
    print("세 개의 정수중 최댓값은 {}입니다.".format(two))
if one > two and three > one:
    print("세 개의 정수중 최댓값은 {}입니다.".format(three))
