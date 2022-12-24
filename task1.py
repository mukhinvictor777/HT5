"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open('user_text.txt', 'w', encoding='utf-8')
line = input('Введите строку\n')
print("Для окончания ввода строк, ввкдите пустую строку")
while line != '':
    my_file.write(line + '\n')
    line = input('Введите строку\n')
my_file.close

my_file = open('user_text.txt', 'r', encoding='utf-8')
for line in my_file:
    print(line)
