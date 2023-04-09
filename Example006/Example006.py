# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
digit = int(input('Введите номер билета: '))
firstPart = digit//1000
secondPart = digit % 1000
firstSum = 0
secondSum = 0
while firstPart > 0 and secondPart > 0:
    x1 = firstPart % 10
    x2 = secondPart % 10
    firstSum += x1
    secondSum += x2
    firstPart //= 10
    secondPart //= 10
if firstSum == secondSum:
    print('Yes')
else:
    print('No')
