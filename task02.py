# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

str = input("Введите трехзначное число ")
print(f"Сумма цифр числа {str} равна {int(str[0]) + int(str[1]) + int(str[2])}")