import datetime

now = datetime.datetime.now()

print("1. 가디언즈 오브 갤럭시 : 10000원")
print("2. 스즈메의 문단속 : 11000원")
print("3. 드림 : 12000원")

what = int(input("시청을 원하는 영화의 번호를 입력해주세요 : "))

if now.hour <= 5:
    print("영화 상영시간이 아닙니다")

if now.hour == 6 <= 8:
    if what == 1:
        print("가디언즈 오브 갤럭시 영화 가격은 9000원 입니다")
    elif what == 2:
        print("스즈메의 문단속 영화 가격은 9900원 입니다")
    elif what == 3:
        print("드림 영화 가격은 10800원 입니다")
else:
    if what == 1:
        print("가디언즈 오브 갤럭시 영화 가격은 10000원 입니다")
    elif what == 2:
        print("스즈메의 문단속 영화 가격은 11000원 입니다")
    elif what == 3:
        print("드림 영화 가격은 12000원 입니다")
