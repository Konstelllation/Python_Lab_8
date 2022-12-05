#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def select_students(staff):
    """
    Выбрать двоечников.
    """
    # Сформировать список студентов.
    result = []
    for student in staff:
        if 2 in list(map(int, student.get('score', '').split())):
            result.append(student)

    # Возвратить список выбранных студентов.
    return result