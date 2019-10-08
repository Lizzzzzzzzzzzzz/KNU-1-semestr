a = int(input("Введіть а"))
b = int(input("Введіть b"))
result = 0
if a > b:
    result = a - b
elif b > a:
    result = a + b
elif a == b:
    result = a
print(result)