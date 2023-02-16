from random import randint
worker_list = []
count = int(input('Введите количество сотрудников: '))
while count > 0:

    worker = randint(0, 100)
    print(f'ID сотрудника: {worker}')
    worker_list.append(worker)
    print()
    count -= 1

print('Текущий список сотрудников:', worker_list)
worker_id = int(input('Какого сотрудника (ID) ищем? '))
for id in worker_list:
    if id == worker_id:
        print(f'ID сотрудника: {id}, сотрудник на работе')
        break
    else:
        print('Сотрудник не работает')
