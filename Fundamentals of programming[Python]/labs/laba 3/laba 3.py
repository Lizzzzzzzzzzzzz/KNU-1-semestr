acc = int(input("Введіть точність"))
k = 1
sum1 = 0
x = 1
if (x**k + k**x != 0):
    for x in range (6):
        while k != acc:
            sum1 += ((2*k - 1) / (2*k)) / (x**k + k**x)
            k += 1
            print(k ,sum1)
else:
    print("знаменник не може бути 0")

