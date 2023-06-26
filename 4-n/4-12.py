string = input("문자열을 입력하세요: ")
space_count = 0
digit_count = 0
letter_count = 0

for char in string:
    if char == " ":
        space_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print("공백의 개수: ", space_count)
print("숫자의 개수: ", digit_count)
print("문자의 개수: ", letter_count)