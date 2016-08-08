#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from my_db_tools.get_data_from_db import get_data
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    # test_list = [item for item in get_data("sxb")]
    return render(request, 'home_test.html')


def product(request):
    # return json data
    response_data = dict()
    response_data['data'] = [item for item in get_data('wq')]
    return JsonResponse(response_data)


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
    response_data['data'] = [item for item in get_data('sxz')]
    return JsonResponse(response_data)


def sxz(request):
    return render(request, 'sxz.html')