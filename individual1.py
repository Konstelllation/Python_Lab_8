#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from individual1_file import strok

if __name__ == '__main__':
    my_list = [
        'строка_1',
        'строка_2',
        'строка_3',
        'строка_4'
    ]
    result = strok()
    print(result(my_list))