#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
from individual2_files.def_get_student import get_student
from individual2_files.def_display_students import display_students
from individual2_files.def_select_students import select_students

def main():
    """
    Главная функция программы.
    """
    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            student = get_student()

            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('fio', ''))

        elif command == 'list':
            # Отобразить всех студентов.
            display_students(students)

        elif command.startswith('select '):
            # Выбрать двоечников
            selected = select_students(students)
            # Отобразить выбранных студентов
            display_students(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select двоечники - запросить двоечников;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()