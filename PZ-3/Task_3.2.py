#При открытии вклада в банке установлены следующие годовые проценты: при
#вкладе до 50000р. процент составит 4%; при вкладе от 50000р. до 100000р. процент
#составит 5%; при вкладе от 100000р. до 150000р. скидка составит 6%; при вкладе от
#150000 р. до 200000 р. процент составит 7%. Составить программу, определяющую
#процентной ставки в зависимости от вносимой суммы.
summa = int(input("Введите сумму вклада: "))
#создаем алгоритм для проверки процентной ставки
if summa < 0:
    print("Повторите ввод.")
    exit()
elif summa < 50000:
    procent = 4
elif 50000 <= summa < 100000:
    procent = 5
elif 100000 <= summa < 150000:
    procent = 6
elif 150000 <= summa < 200000:
    procent = 7
else:
    procent = 0       # Если сумма больше 200000, процентная ставка не определяется

if procent > 0: #выводим процетную ставку
    print(f"Процентная ставка для суммы {summa} рублей составляет {procent}%.")
else:
    print("Превышена максимальная сумма вклада.")