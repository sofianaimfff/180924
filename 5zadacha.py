# Сумма дробей (часть первая)
# Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).

N = int(input("Введите число: "))
S = 0

for i in range (1 , N + 1):
    S += 1 + i / 10
    print(S)