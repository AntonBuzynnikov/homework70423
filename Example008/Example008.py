# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))
k = int(input('Введите количество долек: '))

if k % m == 0 or k % n == 0:
    print("yes")
else:
    print('no')