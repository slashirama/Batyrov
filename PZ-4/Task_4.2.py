# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
# деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
# то вывести TRUE, если нет — вывести FALSE
def has_odd_digits(n):
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            return True
        n //= 10
    return False

try:
    N = int(input("Введите целое число N: "))
    if N > 0:
        result = has_odd_digits(N)
        print(result)
    else:
        print("Число должно быть больше 0.")
except ValueError:
    print("Ошибка: введено некорректное значение.")


