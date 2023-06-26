ID = input("사용할 아이디를 입력하여 주세요 : ")
if len(ID) > 10:
    print("글자수를 10가자 이내로 아이디를 작성해주세요")

passWord = input("사용할 비밀번호를 입력하여 주세요 : ")
if len(passWord) > 10:
    print("글자수를 10가자 이내로 아이디를 작성해주세요")

if len(ID) < 10 and len(passWord) < 10:
    print("회원가입 성공")
    print("당신의 아이디는 {}이고 비밀번호는 {}입니다".format(ID, passWord))
