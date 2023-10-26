def rectangle():
    a = float(input("Ширина %s: " % figure))
    b = float(input("Высота %s: " % figure))
    print("Площадь: %.2f" % (a * b))


def triangle():
    a = float(input("Основание %s: " % figure))
    h = float(input("Высота %s: " % figure))
    print("Площадь: %.2f" % (0.5 * a * h))


figure = input("1-прямоугльник, 2 треугольник: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
