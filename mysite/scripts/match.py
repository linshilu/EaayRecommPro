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

from recomm.views import init_teacherfigure
from recomm.views import match

def run():
    TeacherFigure.objects.all().delete()
    init_teacherfigure()

    result=match()