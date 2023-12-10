# Вариант 2. Дан список размера N. Найти номера тех элементов список, которые больше своего
# левого соседа, и количество таких элементов. Найденные номера выводить в
# порядке их убывания.

def larger_elements(arr):
    result = []
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            result.append(i)
    result.reverse()
    return result, len(result)

list = [1, 3, 2, 4, 5, 2, 7, 6]
print(list)
indices, count = larger_elements(list)
print("Найденные номера в порядке убывания:", indices)
print("Количество таких элементов:", count)
