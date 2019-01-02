# -*- coding: utf-8 -*-
# 全局变量
from django.conf import settings

def global_var(request):
    return {'ip_address': '"http://192.168.66.128:8000"',
            'file_path': '"/home/zafarizb/InitData/"'
            }

def get_filepath():
    return "/home/zafarizb/InitData/"
