#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from my_db_tools.get_data_from_db import *
from my_db_tools.change_data_in_db import insert_kw, insert_user, remove_item, set_sku
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'index.html')
    # return render(request, 'bootstrap_table_test.html')


def table_test(request):
    # return render(request, 'home.html')
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
    response_data = dict()
    data = [item for item in get_data('wq')]
    response_data = json.dumps(data)
    # return JsonResponse(response_data)
    return HttpResponse(response_data,content_type='application/json; charset=utf8')


def ShangXianBei(request):
    # response_data = dict()
    # response_data['data'] = [item for item in get_data('sxb')]
    # return JsonResponse(response_data)
    data = [item for item in get_data('sxb')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def sxb(request):
    return render(request, 'sxb.html')


def WuQiong(request):
    response_data = dict()
    response_data['data'] = [item for item in get_data('wq')]
    return JsonResponse(response_data)


def wq(request):
    return render(request, 'wq.html')


def ChenHaiYue(request):
    # response_data = dict()
    # response_data['data'] = [item for item in get_data('chy')]
    data = [item for item in get_data('chy')]
    response_data = json.dumps(data)
    # return JsonResponse(response_data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def chy(request):
    return render(request, 'chy.html')


def YangShuLin(request):
    # response_data = dict()
    # response_data['data'] = [item for item in get_data('ysl')]
    # return JsonResponse(response_data)
    data = [item for item in get_data('ysl')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def ysl(request):
    return render(request, 'ysl.html')


def YangManMan(request):
    # response_data = dict()
    # response_data['data'] = [item for item in get_data('ymm')]
    # return JsonResponse(response_data)
    data = [item for item in get_data('ymm')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def ymm(request):
    return render(request, 'ymm.html')


def SongXianZhong(request):
    # response_data = dict()
    # response_data['data'] = [item for item in get_data_20_days('sxz')]
    # return JsonResponse(response_data)
    data = [item for item in get_data('sxz')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def sxz(request):
    return render(request, 'sxz.html')


def TEST(request):
    # response_data = dict()
    # response_data['data'] = [item for item in get_data_20_days('sxz')]
    # return JsonResponse(response_data)
    data = [item for item in get_data_20_days('test')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def test(request):
    return render(request, 'test.html')


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


def add_key_words(request):
    response_data = dict()
    if request.method == "POST":
        # response_data['data'] = [{"msg": "success"}]
        owner = request.POST.get('owner')
        kw = request.POST.get('kw')
        # response_data['data'] = [{"kw": kw, "owner": owner}]
        insert_kw(owner, kw)
        return JsonResponse(response_data)
    else:
        response_data['data'] = [{"msg": "Error! Please Post!"}]
        return JsonResponse(response_data)


def operation_wanted(request):
    response_data = dict()
    if request.method == "POST":
        # response_data['data'] = [{"msg": "success"}]
        itemid = request.POST.get('itemid')
        owner = request.POST.get('owner')
        wanted_product(itemid, owner)
        response_data['data'] = [{"itemid": itemid, "owner": owner}]
        return JsonResponse(response_data)
    else:
        response_data['data'] = [{"msg": "Error! Please Post!"}]
        return JsonResponse(response_data)


def operation_remove(request):
    response_data = dict()
    if request.method == "POST":
        # response_data['data'] = [{"msg": "success"}]
        itemid = request.POST.get('itemid')
        owner = request.POST.get('owner')
        remove_item(itemid, owner)
        response_data['data'] = [{"itemid": itemid, "owner": owner}]
        return JsonResponse(response_data)
    else:
        response_data['data'] = [{"msg": "Error! Please Post!"}]
        return JsonResponse(response_data)


def edit_sku(request):
    response_data = dict()
    if request.method == "POST":
        # response_data['data'] = [{"msg": "success"}]
        itemid = request.POST.get('itemid')
        sku = request.POST.get('sku')
        set_sku(itemid, sku)
        response_data['data'] = [{"itemid": itemid, "sku": sku}]
        return JsonResponse(response_data)
    else:
        response_data['data'] = [{"msg": "Error! Please Post!"}]
        return JsonResponse(response_data)


def wanted(request):
    return render(request, 'wanted.html')


def wanted_json(requset):
    data = [kw for kw in get_wanted()]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def shop(request):
    return render(request, 'shop.html')


def hs_test(request):
    return render(request, 'hs_test.html')


def HS_TEST(request):
    data = [i for i in get_updated_date('test')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def hs_sxb(request):
    return render(request, 'hs_sxb.html')


def HS_SXB(request):
    data = [i for i in get_updated_date('sxb')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def hs_wq(request):
    return render(request, 'hs_wq.html')


def HS_WQ(request):
    data = [i for i in get_updated_date('wq')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def hs_chy(request):
    return render(request, 'hs_chy.html')


def HS_CHY(request):
    data = [i for i in get_updated_date('chy')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def hs_ysl(request):
    return render(request, 'hs_ysl.html')


def HS_YSL(request):
    data = [i for i in get_updated_date('ysl')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def hs_ymm(request):
    return render(request, 'hs_ymm.html')


def HS_YMM(request):
    data = [i for i in get_updated_date('ymm')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def hs_sxz(request):
    return render(request, 'hs_sxz.html')


def HS_SXZ(request):
    data = [i for i in get_updated_date('sxz')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def shop(request):
    return render(request, 'shop.html')


def shop_json(request):
    data = [user for user in get_shop_data()]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def add_user_name(request):
    response_data = dict()
    if request.method == "POST":
        # response_data['data'] = [{"msg": "success"}]
        owner = request.POST.get('owner')
        user = request.POST.get('user_name')
        response_data['data'] = [{"user": user, "owner": owner}]
        insert_user(owner, user)
        return JsonResponse(response_data)
    else:
        response_data['data'] = [{"msg": "Error! Please Post!"}]
        return JsonResponse(response_data)


def sp_sxb(request):
    return render(request, 'sp_sxb.html')


def sp_wq(request):
    return render(request, 'sp_wq.html')


def sp_sxz(request):
    return render(request, 'sp_sxz.html')


def sp_chy(request):
    return render(request, 'sp_chy.html')


def sp_ymm(request):
    return render(request, 'sp_ymm.html')


def sp_ysl(request):
    return render(request, 'sp_ysl.html')


def sp_test(request):
    return render(request, 'sp_test.html')


def SP_SXB(request):
    data = [user for user in get_shop_newly_listed('sxb')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def SP_WQ(request):
    data = [user for user in get_shop_newly_listed('wq')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def SP_CHY(request):
    data = [user for user in get_shop_newly_listed('chy')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')




def SP_YSL(request):
    data = [user for user in get_shop_newly_listed('ysl')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def SP_YMM(request):
    data = [user for user in get_shop_newly_listed('ymm')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')


def SP_SXZ(request):
    data = [user for user in get_shop_newly_listed('sxz')]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json; charset=utf8')

