#!/usr/bin/env python
#encoding:utf-8
# def func(obj1,obj2):
#     return 11
#
# func.short_description="中文"
# actions=[func,]
# for item in actions:
#     if hasattr(item,'short_description'):
#         print(item.short_description,item(1,2))
#     else:
#         print(item.__name__.title(),item(1,2))

from types import FunctionType
def yuhao(obj):
    return "aaa"

list_display = ('user', 'email', yuhao)
for item in list_display:
    if isinstance(item,FunctionType):
        print(item(1))
    else:
        print(item)
