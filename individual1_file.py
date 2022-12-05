#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def strok():
    def ol(spisok):
        li = '</li>\n<li>'.join(spisok)
        return f"<ol>\n<li>{li}</li>\n</ol>"
    return ol
