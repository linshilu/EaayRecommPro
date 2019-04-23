# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
import codecs
import json
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404,render
# These views take parameters
from django.urls import reverse
from django.views import generic
from django.http import StreamingHttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from recomm.models import Assistant,TeacherEssay,Teacher,Student,StudentEssay,Recommendation,TeacherFigure,Relation
from recomm.tools.pdf2txt import PdfTranstorm
from recomm.tools.similarity import  Similarity
from recomm.tools.NLTK_handin import Preprocess_Handin
from recomm.tools.NLTK_essays import Preprocess_Essays
import pandas as pd
import zipfile
from pandas import DataFrame
import numpy as np
import time
from time import sleep
import PyPDF2
from django.core.cache import cache
from recomm.tools.pdf2txt import PdfTranstorm
from recomm.tools.Translate import Translate
import pdfminer
import xlwt
import csv
import mysite.contexts as con

from recomm.views import init_stu,init_relation
not_found = {}
type_error = {}
translate_error = {}

def run():

    stuessay_folder="StudentEssay"
    stuessay_folder_path = os.path.join(con.get_filepath(), "Input/StudentEssay_buchong",stuessay_folder)

    stu_path = os.path.join(con.get_filepath(), "Input", "StudentList.csv")
    stuessay_path = os.path.join(con.get_filepath(), "Input", "StudentEssay_buchong.csv")


    # init students
    stu_path = os.path.join(con.get_filepath(), "Input","StudentList.csv")
    init_stu(stu_path)

    # init relation
    rel_path = os.path.join(con.get_filepath(), "Input/Rules","Relation.csv")
    init_relation(rel_path)

    # init students' essays
    print('Delete student essays table ...')
    StudentEssay.objects.all().delete()
    print('Store student essays ...')
    studentessays = pd.read_csv(stuessay_path, sep=',',encoding='utf_8_sig')
    m = 1
    for i in range(len(studentessays['姓名'])):
    #for i in range(0,6):
        global upload_progressbar
        upload_progressbar = m * 0.01 / len(studentessays['姓名']) * 100
        m = m + 1
        if isinstance(studentessays.iloc[i, 2], str):  # 有论文的项才处理
            id = studentessays.iloc[i, 0]
            sname = studentessays.iloc[i, 1]
            name = sname.strip()
            stitle = studentessays.iloc[i, 2]
            title = stitle.strip()
            title = str(id)+'_'+title

            # read the essay
            try:
                translate_text_filepath = os.path.join(con.get_filepath(), "Input/StudentEssay", title + '_en' + '.txt')
                translate_file = open(translate_text_filepath, encoding='utf-8')
            except FileNotFoundError:
                print('file not found')
                print(sname)
                print(title)
            else:
                translate_text = translate_file.read()[0:10000]
                # store to the database
                student = Student.objects.get(pk=id)
                essay = StudentEssay(student=student, student_essay_title=title, student_essay_text=translate_text)
                essay.save()
                print('#########Save file:###########')
                print(name)
                print(title)

    print('########File Not Found List:########')
    print(not_found)