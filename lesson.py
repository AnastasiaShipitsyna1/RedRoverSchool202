print("lesson#1, task#1.1 2")
print("Hello word!")
print("*************************************************************")

print("lesson#1, task#1.1  3")
user_name = input("Введите ваше имя: ")
print("Hello, {}!".format(user_name))


print("*************************************************************")
print("lesson#1, task#1.1 4")

number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
action = input("Введите действие (+, -, *, /): ")

number1 = float(number1)
number2 = float(number2)

result = None

if action == "+":
    result = number1 + number2
elif action == "-":
    result = number1 - number2
elif action == "*":
    result = number1 * number2
elif action == "/":

    if number2 != 0:
        result = number1 / number2
    else:
        result = "Ошибка: деление на ноль"
else:
    result = "Некорректное действие. Поддерживаются только +, -, *, /."

print("Результат:", result)

print("version#1")
print("*************************************************************")
print("lesson#1, task#1.2 1")
print("*********")
print("*       *")
print("*       *")
print("*********")


print("verion #2")
print("*********\n*       *\n*       *\n*********")


print("*************************************************************")
print("lesson#1, task#1.3")

# # Вводим четырёхзначное число
# number = input("Введите четырехзначное число: ")
#
# # Проверяем, что введенная строка действительно является четырёхзначным числом
# if len(number) != 4 or not number.isdigit():
#     print("Пожалуйста, введите четырёхзначное число.")
# else:
#     # Разбиваем число на отдельные цифры
#     thousands = int(number[0])
#     hundreds = int(number[1])
#     tens = int(number[2])
#     units = int(number[3])
#
#     # Выводим результат
#     print("Тысячи -", thousands)
#     print("Сотни -", hundreds)
#     print("Десятки -", tens)
#     print("Единицы -", units)

#int - это встроенный тип данных в языке программирования Python,
# который представляет целые числа (integer). Когда применяется к строке,
# как в вашем примере, int() преобразует строковое представление числа в целочисленное значение.




