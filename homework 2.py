from random import randint
numbers_list = []
count = int(input('Введите длинну списка: '))
while count > 0:

    number = randint(0, 9)
    numbers_list.append(number)
    print()
    count -= 1

print('Текущий список чисел:', numbers_list)
