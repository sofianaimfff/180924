# Вывод чисел от K до N
# Пользователь вводит числа K и N. Выведите все числа от K до N вĸлючительно.
K = int(input("Введите первое число: "))
N = int(input("Введите второе число: "))

for i in range (K, N + 1):
    print(i)