# num = 5
# if num  == 5:
#     print("five")
# elif num < 5:
#     print("less than 5")
# else:
#     print ("More than 5")


#WHILE

i = 0
while i < 10:
    i = i + 1
    if i == 5:
        continue # пропускает итерацию и переходит к следующей
        #break
    print(i)

y = 5
while y > 0:
    print(y, "Yes")
    y = y-1
print("Run!")

#range - диапазон
#len - длина строки
#list - список


word = "hello"

for symbol in word:
    print(f'{word.index(symbol)} - {symbol}')

