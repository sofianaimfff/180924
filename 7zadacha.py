# Дан ряд
# S = 1 + 1 / (x ** 2) + 1 / (x ** 4) + ⋯ + 1 / (x ** (2i−2)) + ...
# Написать программу, ĸоторая вычисляет сумму первых n членов ряда, с заданным
# значением x.

n = int(input("Кол-во членов ряда: "))
x = int(input("Введите x: "))
S = 0

for i in range(1 , n + 1):
    S += 1 / (x ** ( 2 * i - 2))
    print(S)