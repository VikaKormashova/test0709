Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = int(input())
... # Вычисляем первую цифру числа, разделив на 1000
... first = a // 1000
... # Вычисляем вторую цифру числа, вычитая сначала первую цифру и затем умножая на 10 (для получения десятков)
... second = a // 100 - (a // 1000 * 10)
... # Вычисляем третью цифру числа, вычитая сначала последнюю цифру и затем делая целочисленное деление на 10
... third = (a % 100 - a % 10) / 10
... # Вычисляем последнюю цифру числа, остаток от деления на 10
... last = a % 10
... # Проверяем условие: сумма первой и последней цифры равна разнице второй и третьей цифры
... if first + last == second - third:
...     print('ДА')
... else:
...     print('НЕТ')
... 
