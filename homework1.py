
numbers_list = [3, 7, 5]

while True:

    number = int(input('Новое число: '))

    numbers_list.append(number)

    print('Текущий список чисел:', numbers_list)

    for numbers in numbers_list:

        print(numbers ** 2, numbers ** 3, numbers ** 4)

    print()
