# -*- coding: utf-8 -*-
# 全局变量
from django.conf import settings

def global_var(request):
    return {'ip_address': '"http://127.0.0.1:8000"',
            'file_path': '"/home/xjy/InitData/"'
            }

def get_filepath():
    return "/home/xjy/InitData/"
