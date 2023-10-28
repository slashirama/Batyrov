#Дано целое число A. Проверить истинность высказывания: «Число A является
#нечетным».
def is_palindrome(number):
    # Преобразовать число в строку для сравнения символов
    number_str = str(number)

    # Сравнить строку с её обратной версией
    return number_str == number_str[::-1]


# Ваше четырехзначное число
your_number = int(input("Введите четырехзначное число: "))

# Проверить, является ли число палиндромом
if is_palindrome(your_number):
    print(f"{your_number} - это палиндром!")
else:
    print(f"{your_number} - это не палиндром.")