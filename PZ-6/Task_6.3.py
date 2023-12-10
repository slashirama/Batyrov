# Вариант 2. Дан список размера N. Обнулить элементы списка, расположенные между его
# минимальным и максимальным элементами (не включая минимальный и
# максимальный элементы).

numbers = [3, 8, 2, 7, 1, 6, 4, 5]
print(numbers)

# Индексы минимального и максимального элементов
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Обнуление элементов между минимальным и максимальным элементами
if min_index < max_index:
    for i in range(min_index + 1, max_index):
        numbers[i] = 0
else:
    for i in range(max_index + 1, min_index):
        numbers[i] = 0

print(numbers)
