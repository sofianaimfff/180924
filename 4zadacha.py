# Сумма четных от K до N
# Пользователь вводит числа K и N. Выведите сумму тольĸо четных чисел от K до N
# вĸлючительно.

K = int(input("Введите первое число: "))
N = int(input("Введите второе число: "))
d = 0

if K % 2 != 0:
    K += 1

for i in range(K, N + 1, 2):
    d += i
    print("Сумма четных от K до N: " , d )
