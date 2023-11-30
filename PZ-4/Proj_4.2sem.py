# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
# деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
# то вывести TRUE, если нет — вывести FALSE
N = int(input('Введите целое число N: '))
has_odd_digits = False

while N > 0:
    digit = N % 10
    if digit % 2 != 0:
        has_odd_digits = True

    N //= 10
    print(has_odd_digits)


