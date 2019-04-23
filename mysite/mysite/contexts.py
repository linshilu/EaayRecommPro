# -*- coding: utf-8 -*-
# 全局变量
from django.conf import settings

def global_var(request):
    return {'ip_address': '"http://172.18.218.95:8001"',
            'file_path': '"/home/lsl/InitData/"'
            }

def get_filepath():
    return "/home/lsl/InitData/"
