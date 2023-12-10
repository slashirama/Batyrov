# Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
# расставлены правильно (то есть каждой открывающей соответствует одна
# закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
# в которой расположена первая ошибочная закрывающая скобка, или, если
# закрывающих скобок не хватает, число —1.
def check_brackets(s):
    # Инициализация пустого стека
    stack = []

    # Итерация по символам строки с учётом их позиции (start=1)
    for i, char in enumerate(s, start=1):
        # Если символ - открывающая скобка, добавляем её в стек вместе с позицией
        if char == '(':
            stack.append((char, i))
        # Если символ - закрывающая скобка
        elif char == ')':
            # Если стек пуст, возвращаем позицию ошибочной закрывающей скобки
            if not stack:
                return i  # Закрывающая скобка без пары
            # Иначе удаляем последнюю открывающую скобку из стека
            stack.pop()

    # После завершения цикла проверяем, остались ли несогласованные открывающие скобки
    if not stack:
        return 0  # Все скобки согласованы
    else:
        # Если остались, возвращаем позицию первой открывающей скобки без закрывающей
        return stack[-1][1]  # Первая открывающая скобка без закрывающей

# Пример использования
input_string = "a(b)c)d"
result = check_brackets(input_string)

# Вывод результата
if result == 0:
    print("Скобки расставлены правильно.")
elif result == -1:
    print("Недостаточно закрывающих скобок.")
else:
    print(f"Ошибка на позиции {result}.")
