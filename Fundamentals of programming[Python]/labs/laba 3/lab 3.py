import math

accuracy = float(input("Введіть точність: "))
res = 0
result = 0
startCount = 1/2
a = 1
b = 1
upper = 0
flag = True
lowerEx = 0
for x in range(0, 5):
    k = 0
    currentRes = 0
    lowerEx = x ** k + k ** x
    while flag:
        if (lowerEx) == 0:
            print("на 0 неможна ділити")
            flag = False
        else:
            while(upper != ((2k-1) / 2k)):
                upper = startCount * (a/b)
                result = upper/lowerEx
                a += 2
                b += 2
                print(result)
        res += 1

    if(res == accuracy):
        print("розрахунки завершено")
        break











