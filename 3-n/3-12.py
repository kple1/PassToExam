shooting = int(input("사격점수를 입력하시오 : "))
sit_up = int(input("윗몸일으키기 횟수를 입력하시오 : "))
push_ups = int(input("팔굽혀펴기 점수를 입력하시오 : "))

if shooting > 18 and sit_up > 86 and push_ups > 72:
    print("당신은 특급전사 입니다.")

if shooting < 18 and sit_up < 86 and push_ups < 72:
    result_Shoot = 18 - shooting
    result_Sit_Up = 86 - sit_up
    result_Push_Ups = 72 - push_ups
    print("당신은 사격 {}개, 팔굽혀펴기 {}개, 윗몸일으키기 {}개 부족해서 특급전사가 아닙니다".format(result_Shoot, result_Sit_Up, result_Push_Ups))

elif shooting < 18 and sit_up < 86:
    result_Shoot = 18 - shooting
    result_Sit_Up = 86 - sit_up
    print("당신은 팔굽혀펴기는 합격했으나 사격 {}개, 팔굽혀펴기 {}개 부족해서 특급전사가 아닙니다"
          .format(result_Shoot, result_Sit_Up))

elif shooting < 18 and push_ups < 72:
    result_Shoot = 18 - shooting
    result_Sit_Up = 86 - push_ups
    print("당신은 윗몸일으키기는 합격했으나 사격 {}개, 윗몸일으키기 {}개 부족해서 특급전사가 아닙니다"
          .format(result_Shoot, result_Sit_Up))

elif sit_up < 86 and push_ups < 72:
    result_Push_Ups = 72 - shooting
    result_Sit_Up = 86 - push_ups
    print("당신은 사격은 합격했으나 윗몸일으키기 {}개, 팔굽혀펴기 {}개 부족해서 특급전사가 아닙니다"
          .format(result_Sit_Up, result_Push_Ups))

elif shooting < 18:
    result = 18 - shooting
    print("당신은 윗몸일으키기와 팔굽혀펴기는 합격했으나 사격 {}개가 부족해서 특급전사가 아닙니다"
          .format(result))

elif sit_up < 86:
    result = 86 - sit_up
    print("당신은 사격과 팔굽혀펴기는 합격했으나 윗몸일으키기 {}개가 부족해서 특급전사가 아닙니다"
          .format(result))

elif push_ups < 72:
    result = 72 - push_ups
    print("당신은 사격과 윗몸일으키기는 합격했으나 팔굽혀펴기 {}개가 부족해서 특급전사가 아닙니다"
          .format(result))
