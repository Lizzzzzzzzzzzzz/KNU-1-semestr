
~~~~
                                                    Лабораторна робота №1     

Автор:Прохорчук Дмитро Сергійович
Група:ІПЗ-13
Варіант:18
~~~~
Запросити у користувача два числа.  Якщо перше більше другого, то обчислити їх різницю і вивести дані на друк.  Якщо друге число більше першого, то обчислити їх суму і вивести на друк. Якщо обидва числа рівні, то вивести це значення на друк

                                   
                                                    Завдання 1



![схема  до завдання](https://imgur.com/4fd878ba-7495-45ca-a79d-524f0d12ffe4)

    a = int(input("Введіть а"))
    b = int(input("Введіть b"))
    result = 0
    if a > b:
        result = a - b
        print(result)
    elif b > a:
        result = a+b
    elif a == b:
        result = a
    print(result)

    
~~~~
                                                    Текстові данні 

a:400
b:30

~~~~

 
