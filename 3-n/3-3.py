work_time = input("일주일간의 근무시간을 입력하세요(hh:mm): ")
hour, minute = work_time.split(":")
hour = int(hour)
minute = int(minute) / 2

hourly_wage = int(input("시급을 입력하세요: "))

if hour > 60 or minute > 30:
    print("시간 입력부분에서 분의 입력값이 잘못되었습니다. (0 ~ 60) 범위 입력")
else:
    total_hours = hour + minute / 60  # 시간과 분을 합산하여 총 근무시간 계산
    if total_hours > 40:
        total_wage = 40 * hourly_wage + (total_hours - 40) * 1.5 * hourly_wage
    else:
        total_wage = total_hours * hourly_wage

    print("당신의 급여는 {}원 입니다".format(total_wage))
