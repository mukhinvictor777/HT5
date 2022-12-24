"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк)
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('task3.txt', 'r', encoding='utf-8') as file:
    employees = file.readlines()
    sum = 0
    for i in range(len(employees)):
        employee = employees[i].split()
        salary = float(employee[1])
        sum += salary
        if salary < 20000:
            print(f"{employee[0]} -> {employee[1]}")
    print(f"Средняя величина дохода сотрудников: {round(sum/len(employees), 2)}")
