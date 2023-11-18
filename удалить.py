import numpy as np


import logging
import logging.config


def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    dictLogConfig = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": "config2.log"
            }
        },
        "loggers": {
            "exampleApp": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("exampleApp")
    logger.info("Program started")
    logger.info("Done!")


if __name__ == "__main__":
    main()




logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

n = int(input('Задайте количесвто в мешке бочонков: '))

array = []
new_array = []

for i in range(1, n+1):
    array.append(i)

new_str = ''
while len(array) != 0:
    if input('Нажатие ENTER, чтобы вытащить случайный бочонок из мешка') == '':
        random = np.random.randint(0, len(array))
        number = array[random]
        print(f'Вам выпало число: {number}')
        logging.debug(f'Бочонок {number} вытащен из мешка')


        new_array.append(number)
        array.pop(random)

for i in range(0, len(new_array)):
    new_str += str(new_array[i])
    if i + 1 == len(new_array):
        new_str += '. '
    else:
        new_str += ', '

logging.debug(f'Вы вытащили из мешка бочонки с числами: {new_str}')