#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def render(file):
    print("Content-type: text/html;charset=utf-8")
    print()
    text = u""
    _default = open('default_view.html', 'r')
    default = _default.read()
    default_upper = default.split('(__SiteContent)')[0]
    default_lower = default.split('(__SiteContent)')[1]
    text += default_upper
    html_file = open(file, 'r')
    text += html_file.read()
    html_file.close()
    _default.close()
    text += default_lower
    print(text)


render('views/hello.html')
