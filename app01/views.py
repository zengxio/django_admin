from django.shortcuts import render

# Create your views here.

from django.template.response import TemplateResponse
def test(request):
    """django admin原理"""
    """默认访问我们自定制的页面，如果没有在访问自带的"""
    return TemplateResponse(request,[] or ['xiaohaohao.html','my_change_list.html'],{'k1':'v1'})
