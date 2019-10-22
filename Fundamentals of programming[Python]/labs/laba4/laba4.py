

i: float = -2
def sinh(x):
    toc = float(input("Введіть точність"))
    sum = x
    item = x
    i = 2
    while abs(item) > toc:
        item *= x**(2*i) /i*(i-1)
        sum += item
        i += 2
    return sum

def value(i):
    if i <= :
        return float("NaN")
    elif  0 <= i <= 1:
        sinh(arg)
    else:
        return float("NaN")


while i <= 2:
    print(value(3))
    i += 0.5