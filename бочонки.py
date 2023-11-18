import numpy as np
import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug('Программа запущена')

n = 0
while n <= 0:
    flag = 0
    # чтобы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
    try:
        n = int(input('Задайте количество в мешке бочонков: '))
    except ValueError:
        print("\033[31m" + "Количество бочонков в мешке должно быть задано числом !!!" + "\033[0m")
        n = 0
        logging.error('Количество бочонков в мешке задано не числом !!!')
        flag = 1
        pass

    if n <= 0 and flag == 0:
        print("\033[31m" + "Количество бочонков в мешке должно быть задано положительным числом !!!" + "\033[0m")
        logging.error('Количество бочонков в мешке задано не положительным числом !!!')
logging.info('Задано количество бочонков в мешке')
#  Бочонки в мешке
array = []
#  Вытащенные бочонки
new_array = []
#  Заполняем мешок бочонками от 1 до n
for i in range(1, n+1):
    array.append(i)
    logging.info(f'Добавлен бочонок {i} в мешок')

new_str = ''
while len(array) != 0:
    if input('Нажмите на ENTER, чтобы вытащить случайный бочонок из мешка ') == '':
        random = np.random.randint(0, len(array))
        print(f'вам выпало число: {array[random]}')
        logging.info(f'Бочонок {array[random]} вытащен из мешка')
        #  Добавляем вытащенный бочонок в новый массив
        new_array.append(array[random])
        #  Удаляем бочонок из старого массива
        array.pop(random)
    else:
        print("\033[31m" + "Нажмите на ENTER !!!"  + "\033[0m")
        logging.error('Пользователь нажал кнопку отличную от ENTER, чтобы вытащить случайный бочонок из мешка !!!')

#  Переводим массив в строку
for i in range(0, len(new_array)):
    new_str += str(new_array[i])
    if i + 1 == len(new_array):
        new_str += '. '
    else:
        new_str += ', '
logging.info(f'массив с бочонками переведен в строку')

print(f'Вы вытащили из мешка бочонки с числами: {new_str}')
logging.info(f'Из мешка были вытащены бочонки с числами: {new_str}')
logging.debug('Программа завершена')