List = [[1, 2, 3], 5, 6, [7, 8]]
for i in List:
    if type(i) is list:
        for j in i:
            print(j, end=" ")
    else:
        print(i, end=" ")

    #if type(i) != list:
    #print(i, end=" ")
