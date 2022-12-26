"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

numbers = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'
           }
new_numbers = []
digit = []
file = open('task4.txt', 'r', encoding="utf-8")
russian_numbers = open('russian_numbers.txt', 'r+', encoding="utf-8")
line = file.readlines()
for el in line:
    num = el.split()
    new_numbers.append(num[0])
    digit.append(num[2])
print(new_numbers)
for i in range(len(new_numbers)):
    russian_numbers.write(numbers[new_numbers[i]])
    russian_numbers.write(" - ")
    russian_numbers.write(digit[i] + "\n")











#    russian_numbers.writelines(new_numbers)
#for i in russian_numbers:
#    print(i)
