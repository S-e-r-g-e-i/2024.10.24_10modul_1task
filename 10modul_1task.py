# Домашнее задание по теме "Создание потоков"
from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf8')
    for i in range(1, word_count + 1):
        file.write(f'Какое-то слово №{i}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}') # ушло примерно 34 сек


time_start_1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start_1
print(f'Работа потоков V1: {time_res_1}')

time_start_2 = datetime.now()
thr_5 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_6 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_7 = Thread(target=write_words, args=(200, 'example7txt'))
thr_8 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()

thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()
time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
print(f'Работа потоков V2: {time_res_2}') # ушло примерно 20 сек

