# Задача 2: Найдите сумму цифр трехзначного числа.
digit = int(input('Введите число: '))
sum = 0
while digit > 0:
    x = digit % 10
    digit = digit//10
    sum = sum + x
print(sum)
