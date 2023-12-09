def mean(x, y):
    arithmetic_mean = (x + y) / 2
    geometric_mean = (x * y) ** 0.5
    return arithmetic_mean, geometric_mean

A = 5
B = 8
C = 12
D = 15

mean_AB = mean(A, B)
mean_AC = mean(A, C)
mean_AD = mean(A, D)

print(f"Среднее арифметическое и геометрическое для (A, B): {mean_AB}")
print(f"Среднее арифметическое и геометрическое для (A, C): {mean_AC}")
print(f"Среднее арифметическое и геометрическое для (A, D): {mean_AD}")
