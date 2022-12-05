#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def get_student():
    """
        Запросить данные о студенте.
        """
    fio = input("Фамилия и инициалы: ")
    group = input("Номер группы: ")
    score = input("Успеваемость: ")

    # Создать словарь.
    return {
        'fio': fio,
        'group': group,
        'score': score,
    }