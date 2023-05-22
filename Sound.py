hour, minute = map(int, input().split())
var = minute - 45

if var < 0:
    hour = hour - 1
    result = minute - 45
    minute = result
    print(hour, minute)

if var > 0:
    minute = minute - 45
    print(hour, minute)

if var == 0:
    minute = 0
    print(hour, minute)
