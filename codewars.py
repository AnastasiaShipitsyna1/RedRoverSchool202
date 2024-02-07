#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
def sum_array(arr):
    if arr == 0 or arr is None or arr == [] or len(arr) == 1:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))

    return sum(arr)

your_list = [0, 0]
result = sum_array(your_list)
print(result)

#2
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

#https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python

def stringy(size):
    result = ""

    for i in range(size):
        if i % 2 == 0:
            result += '1'  # Добавляем '1', если индекс четный
        else:
            result += '0'  # Добавляем '0', если индекс нечетный

    return result
print(stringy(5))

#Мы начинаем с пустой строки: result = ''.
# Затем запускается цикл for i in range(size), где size в данном случае равно 6.
# Первая итерация цикла (когда i равно 0): Так как 0 четное число, мы добавляем '1' к result: result += '1'.
# Теперь result становится '1'.
# Вторая итерация (когда i равно 1): Так как 1 нечетное число, мы добавляем '0' к result: result += '0'.
# Теперь result становится '10'.
# Третья итерация (когда i равно 2): Так как 2 четное число, мы добавляем '1' к result: result += '1'.
# Теперь result становится '101'.
# И так далее, пока не достигнем 6 итераций.


#тот же пример
def stringy(size):
    return ('10' * size)[:size]





#https://www.codewars.com/kata/557b5e0bddf29d861400005d/train/python
def converter(mpg):
    # Коэффициенты для преобразования
    miles_to_kilometers = 1.609344
    gallons_to_liters = 4.54609188

    kilometers = mpg * miles_to_kilometers

    # Объем топлива в литрах
    liters = 1 / gallons_to_liters  # Используем 1 галлон, так как мы рассматриваем "на один галлон"

    # Вычисление километров на литр и округление до двух знаков после запятой
    kilometers_per_liter = kilometers * liters
    result = round(kilometers_per_liter, 2)

    return result

    # Пример использования:
mpg_input = 30  # Введите свое значение в милях на галлон
kpl_output = converter(mpg_input)
print(f'{mpg_input} mpg равно {kpl_output} kpl')

# короткое решение:

def converter(mpg):
    #your code here
    return round(mpg / 4.54609188 * 1.609344    , 2)



 # https://www.codewars.com/kata/56b29582461215098d00000f

def pipe_fix(nums):
    min_num = min(nums)
    max_num = max(nums)

    return list(range(min_num, max_num + 1))

#тот же пример

def pipe_fix(nums):
	return list(range(nums[0], nums[-1] + 1))

#https://www.codewars.com/kata/57356c55867b9b7a60000bd7

def basic_op(operator, value1, value2):
    if operator == "+":
        result = value1 + value2

    elif operator == "-":
        result = value1 - value2

    elif operator == "*":
        result = value1 * value2

    elif operator == "/":
        result = value1 / value2

    return result



# https://www.codewars.com/kata/57280481e8118511f7000ffa

#split()может разделить строку на несколько частей с помощью указанного разделителя.
string = "My name is John"
words = string.split(" ")
print(words)
# Output:
# ['My', 'name', 'is', 'John']


string = "My name is John"
words1 = string.split(" ", 3)
print("words1:", words1)
words2 = string.split(" ", 5)
print("words2:", words2)
#output:
words1:[ 'My', 'name', 'is' ]
words2:[ 'My', 'name', 'is', 'John' ]



string = "My name is John"
words = list(string)
print(words)
['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'J', 'o', 'h', 'n']


str = "My" + "name" + "is" + "John"
print(str)
#or
str = "".join(["My", "name", "is", "John"])
print(str)

#result
MynameisJohn

# решение правильное:

def split_and_merge(string, separator): #Функция split_and_merge принимает два параметра: string (входная строка) и separator (символ, который будет использоваться в качестве разделителя).
    words = [separator.join(list(word)) for word in string.split()]# список
    return " ".join(words) #Эта строка объединяет все измененные "слова" обратно в предложение с использованием пробелов в качестве разделителей.

#string.split(): Этот фрагмент кода разделяет входную строку на список слов. Метод split() без аргументов разделяет строку по пробелам.
# for word in string.split(): Это списковое включение, которое перебирает каждое слово в списке слов. for word in ...: Создает цикл for, который итерирует по элементам последовательности.
# В этом контексте in используется для итерации по элементам последовательности, в данном случае, по элементам, полученным после разделения строки string методом split().
#separator.join(list(word)): Для каждого слова этот фрагмент кода разбивает слово на список символов, а затем снова объединяет их с использованием указанного separator.

# еще одно правильное решение
def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())

#неправильно но тоже полезно знать:

def split_and_merge(string_, separator):
     words = list(string_)
     merge_string = separator.join(words)
     return merge_string

#words = list(string_): Здесь string_ — это строка, переданная функции в качестве аргумента. Метод list() используется для преобразования строки в список.
# Это означает, что каждый символ строки будет отдельным элементом списка. Например, если string_ равно "My name", то words будет равно ['M', 'y', ' ', 'n', 'a', 'm', 'e'].

#merged_string = separator.join(words): Здесь используется метод join(), который объединяет элементы списка (words) в строку,
# вставляя между ними разделитель (separator). Таким образом, если separator равен пробелу, то merged_string будет строкой, где символы из words объединены пробелами.
# Если separator равен "/", то символы объединяются символами "/" между ними.


def split_and_merge(string_, separator):
    words = []
    for char in string_:
        if char.isalpha():
            words.append(char)
        else:
            words.append(separator)
    return "".join(words)

#char.isalpha() - это метод строки в Python, который возвращает True, если все символы в строке являются буквами (буквенными символами), и False в противном случае.
#Таким образом, строка char.isalpha() в условии if проверяет, является ли текущий символ (char) буквенным символом.
# Если char - буквенный символ, то условие if истинно (True), и символ добавляется в список words с использованием words.append(char).
#Это условие используется для того, чтобы добавить в список words только буквенные символы из исходной строки.
# В противном случае (если char не является буквенным символом), добавляется разделитель (заданный переменной separator)


#words.append(char) - это операция добавления символа char в конец списка words. Метод append() в Python используется для добавления элемента в конец списка.
#В контексте вашей функции split_and_merge, каждый буквенный символ из строки string_ добавляется в список words. Этот список впоследствии объединяется в строку с использованием метода "".join(words).

# https://www.codewars.com/kata/57241e0f440cd279b5000829

#Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples
# Examples
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"

def sum_mul(n, m):
    # Проверка на натуральные числа
    if n <= 0 or m <= 0:
        return "INVALID"

    # Инициализация суммы
    total_sum = 0

    # Перебор чисел от n до m с шагом n
    for i in range(n, m, n):
        # Добавление к сумме
        total_sum += i

    return total_sum


#еще одно решение:
def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'

# https://www.codewars.com/kata/58261acb22be6e2ed800003a
def get_volume_of_cuboid(length, width, height):
    result = length * width *height
    return(result)

# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
#Ваш код покажет полное имя соседа и сокращенную версию имени в виде массива. Если количество символов в имени меньше или равно двум, он вернет массив, содержащий только имя как есть"
def who_is_paying(name):
    # Проверка, что имя не пустое
    if len(name) <= 0:
        return [name]

    # Проверка, что количество символов в имени больше 2
    if len(name) > 2:
        # Вернуть полное имя и сокращенную версию в виде массива
        return [name, name[:2]]
    else:
        # Вернуть массив, содержащий только имя как есть
        return [name]

#еще одно решение:
def who_is_paying(name):
    return [name,name[0:2]] if len(name)>2 else [name]


# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b
# In this kata you will create a function that takes in a list and returns a list with the reverse order.
#
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    return l[::-1] #==> срезы

# Срезы (slices) в Python - это способ получения подмножества элементов из последовательности, такой как строка, список или кортеж. Синтаксис срезов выглядит следующим образом:

# sequence[start:stop:step]

# Где:
# - `start` - индекс начала среза (включительно).
# - `stop` - индекс конца среза (исключительно).
# - `step` - шаг, с которым извлекаются элементы.
#
# Элементы извлекаются из последовательности, начиная с индекса `start` и до, но не включая, индекса `stop`, с использованием указанного шага.

my_list = [1, 2, 3, 4, 5]

# Извлечение элементов с индексами 1 до 3 (не включая 3)
subset = my_list[1:3]
# subset содержит [2, 3]

# Извлечение каждого второго элемента с индексами 0 до 4
subset = my_list[0:5:2]
# subset содержит [1, 3, 5]

# Извлечение обратного порядка элементов
reverse_list = my_list[::-1]
# reverse_list содержит [5, 4, 3, 2, 1]


# https://www.codewars.com/kata/5875b200d520904a04000003


def enough(cap, on, wait):
    if on + wait <= cap:
        return 0
    else:
        return on + wait - cap

# Пример использования:
print(enough(10, 5, 5))  # Вывод: 0 (места достаточно)
print(enough(10, 8, 3))  # Вывод: 1 (не хватает одного места)


def enough(cap, on, wait):
    return wait + on - cap if wait + on > cap else 0


def enough(cap, on, wait):
    return max(0, on + wait - cap)

#Функция max() в Python используется для нахождения максимального значения из переданных ей аргументов или из элементов итерируемого объекта

max_value = max(3, 7, 1, 9, 4) #С использованием аргументов
# max_value содержит 9

my_list = [3, 7, 1, 9, 4]
max_value = max(my_list)
# max_value содержит 9


# https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7
#Напишите функцию, которая преобразует входную строку в верхний регистр.

def make_upper_case(s):
    return s.upper() #метод upper() не принимает аргументов. Метод upper() используется на строке напрямую, то есть в () не указываем s


#В Python, для преобразования всех букв в слове в верхний регистр, вы можете использовать метод строки upper(). Вот пример:

word = "example"
upper_case_word = word.upper()

print(upper_case_word)



# https://www.codewars.com/kata/5601409514fc93442500010b


# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return True if you're better, else False!
#
# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

def better_than_average(class_points, your_points):
    count = len(class_points)
    average = sum(class_points) / count

    if your_points > average:
        return True
    else:
        return False

#еще одно решение:
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# https://www.codewars.com/kata/5808e2006b65bff35500008f

#перевести буквы в цифры, где а=1
def position(alphabet):
    alphabet = alphabet.lower()
    result = []

    for char in alphabet:
        if 'a' <= char <= 'z':
            result.append(str(ord(char) - ord('a') + 1))
        else:
            result.append(char)

    return 'Position of alphabet: ' + ', '.join(result)


#еще одно решение:
def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)



# пример абстрактный
def letters_to_numbers(word):
    word = word.lower()  # Приводим все буквы к нижнему регистру (опционально)
    result = []

    for char in word:
        if 'a' <= char <= 'z':
            # Если символ является буквой, добавляем его порядковый номер
            result.append(ord(char) - ord('a') + 1)
        else:
            # Если символ не является буквой, добавляем его как есть
            result.append(char)

    return result

#В конструкции for char in word: в Python, char представляет собой временную переменную, которая будет принимать значения из итерируемого объекта word на каждой итерации цикла.
# В данном случае, word является строкой, и цикл for будет проходить по каждому символу этой строки.
#Таким образом, на каждой итерации переменная char будет содержать текущий символ строки word.
# Например, если word = "hello", то на первой итерации char будет равен "h", на второй - "e", и так далее, пока не будут обработаны все символы строки.
# result.append(ord(char) - ord('a') + 1) - это часть кода, где происходит добавление значения в список result.
# ord(char): Функция ord() используется для получения числового представления (кода) символа. В данном контексте, ord(char) возвращает числовой код символа char.
# ord('a'): Здесь мы получаем числовой код символа 'a'.
# ord(char) - ord('a') + 1: Это выражение вычисляет разницу между числовым кодом текущего символа и числовым кодом символа 'a'.
# Добавление 1 к результату обеспечивает соответствие номеров букв в алфавите (где 'a' = 1, 'b' = 2 и так далее).
# result.append(...): Метод append() используется для добавления значения в конец списка. В данном случае, результат выражения ord(char) - ord('a') + 1 добавляется в список result.






# https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(s):
    result = ''
    for digit in s:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result



#еще одно решение:
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)



# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
# Write a function to split a string and convert it into an array of words.
#Напишите функцию для разделения строки и преобразования ее в массив слов.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my"
#если строка пустая вернуть [""]

#решение задачи
def string_to_array(s):
    if not s:  # Проверяем, является ли строка пустой
        return [""]

    words = s.split()
    return words


#короткое решение:
def string_to_array(string):
    return string.split(" ")



#на эту же тему:

def quote_each_word(s):
    words = s.split()  # Разбиваем строку на слова
    result = ' '.join(f'"{word}"' for word in words)  # Каждое слово заключаем в кавычки
    return result


#разбор строки
#result = ' '.join(f'"{word}"' for word in words)
#for word in words: Эта часть означает, что мы проходимся по каждому слову в списке words. Предполагается, что words - это список слов в строке.

#f'"{word}"': Это форматированная строка (f-string), которая заключает каждое слово в двойные кавычки.
# f'"{word}"' использует f-string для вставки значения переменной word внутрь строки. Таким образом, каждое слово будет заключено в двойные кавычки.

#' '.join(...): Этот вызов join объединяет каждую строку, созданную в генераторе, в одну строку.
# Строки будут разделены пробелом, так что результат будет выглядеть как одна строка, где каждое слово заключено в двойные кавычки и разделено пробелами.

#Пример:

# words = ["Hello", "world,", "how", "are", "you?"]
# result = ' '.join(f'"{word}"' for word in words)
# print(result)
#
# "Hello" "world," "how" "are" "you?"


