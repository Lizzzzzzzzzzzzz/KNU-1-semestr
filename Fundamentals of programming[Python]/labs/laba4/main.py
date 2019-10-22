import math

x: float = -2
accuracy = float(input('input cycles: '))
i = 0
def formula(x, accuracy):
    x: float = -2
    i = 0
    y = 0
    char = 1
    previous = 1
    while i < accuracy:
        i = 0.5
        form = x**(2*i) /i*(i-1)
        y = 1 / form
        previous = form
        char *= -1
        i += 1
        x += 0.5
    return y

def y(x):
    if x < 0:
        return float('NaN')
    elif 0 < x < 1.5:
        return formula(x, accuracy)
    else:
        return float('NaN')

while x <= 2:
    print(y(x))
    x += 0.5


