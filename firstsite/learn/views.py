#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from my_db_tools.get_data_from_db import get_data, get_kw_data, get_data_20_days
from django.http import JsonResponse
import json

def index(request):
    # return render(request, 'index.html')
    return render(request, 'bootstrap_table_test.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    test_list = [item for item in get_kw_data()]
    return render(request, 'home_test.html',{'test':test_list})


def product(request):
    # return json data
    # response_data = dict()
    data = [item for item in get_data_20_days('wq')]
    response_data = json.dumps(data)
    return HttpResponse(response_data,content_type='application/json; charset=utf8')


def ShangXianBei(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data('sxb')]
    return JsonResponse(response_data)


def sxb(request):
    return render(request, 'sxb.html')


def WuQiong(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data('wq')]
    return JsonResponse(response_data)


def wq(request):
    return render(request, 'wq.html')


def ChenHaiYue(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data('chy')]
    return JsonResponse(response_data)


def chy(request):
    return render(request, 'chy.html')


def YangShuLin(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data('ysl')]
    return JsonResponse(response_data)


def ysl(request):
    return render(request, 'ysl.html')


def YangManMan(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data('ymm')]
    return JsonResponse(response_data)


def ymm(request):
    return render(request, 'ymm.html')


def SongXianZhong(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data_20_days('sxz')]
    return JsonResponse(response_data)


def sxz(request):
    return render(request, 'sxz.html')


def key_words_api(request):
    response_data = dict()
    response_data['data'] = [kw for kw in get_kw_data()]
    # response_data = [kw for kw in get_kw_data()]
    return JsonResponse(response_data)


def key_words_json(request):
    data = [kw for kw in get_kw_data()]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def key_words(request):
    return render(request, 'key_words.html')

