def mean(x, y):
    AMean = (x + y) / 2
    GMean = (x * y) ** 0.5
    return AMean, GMean

try:
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    d = float(input("Введите значение d: "))
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
    exit()

mean_ab = mean(a, b)
mean_ac = mean(a, c)
mean_ad = mean(a, d)

# Вывод результатов
print(f"Среднее арифметическое и геометрическое для (a, b): {mean_ab}")
print(f"Среднее арифметическое и геометрическое для (a, c): {mean_ac}")
print(f"Среднее арифметическое и геометрическое для (a, d): {mean_ad}")

