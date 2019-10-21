import math

x: float = -2
accuracy = float(input('input cycles: '))
i = 0
def formula(x, accuracy):
    i = 0
    y = 0
    char = 1
    previous = 1
    while i < accuracy:
        form = 1 / 2 * (previous + (x**2 - 1) / previous)
        y = 1 / form
        previous = form
        char *= -1
        i += 1
    return y

def y(x):
    if x <= 1:
        return float('NaN')
    elif 1 < x < 2:
        return formula(x, accuracy)
    else:
        return float('NaN')

while x < 2:
    print(y(x))
    x += 0.5


