"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

file = open('new_file.txt', 'w',encoding="utf-8")
file.write("55 66 333 21 65 98 323 65 15 475 45")
file = open('new_file.txt', 'r',encoding="utf-8")
line = file.readlines()
sum = 0
for el in line:
    num = el.split()
for i in range(len(num)):
    sum += int(num[i])
print(f'Сумма всех чисел в файле равна: {sum}')





