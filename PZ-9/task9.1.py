# Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4».
# Преобразовать информацию из строки в словарь,
# найти среднее арифметическое оценок, результаты вывести на экран.
input_string = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"

elements = input_string.split()

student_data = {
    'Фамилия': f"{elements[0]} ",
    'Имя' : f"{elements[1]}",
    'Группа': elements[2],
    'Оценки': list(map(int, elements[3:])),
}

average_grade = sum(student_data['Оценки']) / len(student_data['Оценки'])

print("Информация:")
for key, value in student_data.items():
    print(f"{key}: {value}")

print("Среднее арифметическое оценок:", average_grade)