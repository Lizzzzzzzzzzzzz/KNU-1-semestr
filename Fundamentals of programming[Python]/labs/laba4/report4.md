
~~~~
                                                    Лабораторна робота №4     

Автор:Прохорчук Дмитро Сергійович
Група:ІПЗ-13
Варіант:18
~~~~
                                                          Завдання
~~~~
18.Обчислити значення функції у, розвинувши функцію sh(x) у ряд Тейлора. Аргумент х 
змінюється від -2 до 2 з кроком 0.5. Визначити похибку y 
~~~~                                                                                



![схема  до завдання]()

~~~~
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
~~~~    

                                                    Текстові данні                                                    
~~~~
k = 6
sum1 = 3.8583333333333334   

                                                    Тестування 
from unittest import TestCase
import unittest
import laba3



class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(laba3.sum(), 3.8583333333333334)



if __name__ == "__main__":
    unittest.main()

Ran 1 test in 2.244s

OK