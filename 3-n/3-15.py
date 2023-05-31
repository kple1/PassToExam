sendToMessage = input("보내고 싶은 메세지를 입력하세요 > ")

if len(sendToMessage) <= 10:
    print("당신이 보내고자하는 메세지는 {}글자이며 추가요금은 없습니다".format(len(sendToMessage)))

if 11 <= len(sendToMessage) <= 30:
    print("당신이 보내고자하는 메세지는 {}글자이며 추가요금은 100원 입니다.".format(len(sendToMessage)))

if 31 <= len(sendToMessage) <= 40:
    print("당신이 보내고자하는 메세지는 {}글자이며 추가요금은 200원 입니다.".format(len(sendToMessage)))

if len(sendToMessage) > 40:
    print("당신이 보내고자하는 메세지는 {}글자이며 추가요금은 300원 입니다.".format(len(sendToMessage)))
