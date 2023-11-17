import numpy as np

n = int(input('Задайте количесвто в мешке бочонков: '))
#  Бочонки в мешке
array = []
#  Вытащенные бочонки
new_array = []
#  Заполняем мешок бочонками от 1 до n
for i in range(1, n+1):
    array.append(i)

new_str = ''
while len(array) != 0:
    if input('Нажатие ENTER, чтобы вытащить случайный бочонок из мешка') == '':
        random = np.random.randint(0, len(array))
        print(f'вам выпало число: {array[random]}')
        #  Добавляем вытащенный бочонок в новый массив
        new_array.append(array[random])
        #  Удаляем бочонок из старого массива
        array.pop(random)

#  Переводим массив в строку
for i in range(0, len(new_array)):
    new_str += str(new_array[i])
    if i + 1 == len(new_array):
        new_str += '. '
    else:
        new_str += ', '

print(f'Вы вытащили из мешка бочонки с числами: {new_str}')