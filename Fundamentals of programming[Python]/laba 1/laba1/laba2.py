a = int(input("Введіть а"))
b = int(input("Введіть b"))
result = 0
if a > b:
    result = a - b
    print(result)
elif b > a:
    result = a+b
    print(result)
elif a == b:
    result = a
    print(result)