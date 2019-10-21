def sum():
    sum1 = 0
    k = 1
    x = 1
    acc = int(input("Введіть точність"))
    if (x**k + k**x != 0):
        for x in range (6):
            while k != acc:
                sum1 += ((2*k - 1) / (2*k)) / (x**k + k**x)
                k += 1
                print(k ,sum1)
    else:
        print("знаменник не може бути 0")
    return sum1
