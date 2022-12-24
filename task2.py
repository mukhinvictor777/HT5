"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open("task2.txt", 'r', encoding='utf-8')
str_list = file.readlines()
print(f'Количество строк в файле {len(str_list)}')
for i in range(len(str_list)):
    word = str_list[i].split()
    print(f'В {i + 1}-ой строке {len(word)} слов')
