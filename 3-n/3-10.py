print("떡볶이 : 4000원")
print("순대 : 5000원")
print("튀김세트 : 7000원")

ddeokBBoks = int(input("떡볶이는 몇 인분을 주문하시겠습니까? : "))
sunDae = int(input("순대는 몇 인분을 주문하시겠습니까? : "))
twiGim = int(input("튀김세트는 몇 인분을 주문하시겠습니까? : "))
age = int(input("나이를 입력하여 주세요 : "))

result1 = ddeokBBoks * 4000 + sunDae * 5000 + twiGim * 7000

teenager = result1 - (result1 * 0.3)
twenties = result1 - (result1 * 0.2)
thirties = result1 - (result1 * 0.1)

if 10 <= int(age) < 20:
    print("떡볶이 {}인분, 순대 {}인분, 튀김세트 {}인분을 구매하셨음으로\n"
          "지불하실 금액은 {}원이지만 30% 할인 적용 되어 {}입니다.".format(ddeokBBoks, sunDae, twiGim, result1, teenager))

elif 20 <= int(age) < 30:
    print("떡볶이 {}인분, 순대 {}인분, 튀김세트 {}인분을 구매하셨음으로\n"
          "지불하실 금액은 {}원이지만 20% 할인 적용 되어 {}입니다.".format(ddeokBBoks, sunDae, twiGim, result1, twenties))

elif 30 <= int(age) < 40:
    print("떡볶이 {}인분, 순대 {}인분, 튀김세트 {}인분을 구매하셨음으로\n"
          "지불하실 금액은 {}원이지만 10% 할인 적용 되어 {}입니다.".format(ddeokBBoks, sunDae, twiGim, result1, thirties))

else:
    print("떡볶이 {}인분, 순대 {}인분, 튀김세트 {}인분을 구매하셨음으로\n"
          "지불하실 금액은 {}원입니다".format(ddeokBBoks, sunDae, twiGim, result1))
