"""
Оглянемся назад
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""
el_1 = int(input())
el_2 = int(input())
while el_2 > 0:
    el_1, el_2 = el_2, el_1 % el_2
print(el_1)
