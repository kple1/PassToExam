age = int(input("나이를 입력해주세요 : "))

if age < 19:
    print("구매불가 20세 되서 와요^^")

elif age > 19:
    print("1. 술 : 1600원\n"
          "2. 담배 : 4500원")

    alcohol = input("술 구입 개수 : ")
    smoke = input("담배 구입 개수 : ")
    payment = input("결제 방식을 입력해 주세요 (카드 or 현금)")
    result = 1600 * int(alcohol) + 4500 * int(smoke)
    sale = result - (result * 0.05)
    main = result - sale

    if payment == "현금":
        print("술 {}병 담배 {}갑을 구매하여서 총 금액은 {}원 이지만,\n"
              "5%할인({}) 되어 {}원입니다."
              .format(alcohol, smoke, result, main, sale))

    else:
        print("술 {}병 담배 {}갑을 구매하여서 총 금액은 {}원 입니다"
              .format(alcohol, smoke, result))
