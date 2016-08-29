"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', learn_views.home, name='home'),
    url(r'^index/$', learn_views.index, name='index'),
    # url(r'^index/key_words_json', learn_views.key_words_json, name='test_kw'),
    url(r'^table/$', learn_views.table_test, name='table'),
    url(r'^table/key_words_json', learn_views.key_words_json, name='test_kw'),
    url(r'^add/$', learn_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^operation_wanted/', learn_views.operation_wanted, name='operation_wanted'),
    url(r'^operation_remove/', learn_views.operation_remove, name='operation_remove'),
    url(r'^index/product', learn_views.product, name='product'),
    # url(r'^index/ShangXianBei',learn_views.ShangXianBei,name="SXB"),
    url(r'^sxb/$', learn_views.sxb, name='sxb'),
    url(r'^sxb/ShangXianBei/', learn_views.ShangXianBei, name='ShangXianBei'),
    url(r'^wq/$', learn_views.wq, name='wq'),
    url(r'^wq/WuQiong/', learn_views.WuQiong, name='WuQing'),
    url(r'^chy/$', learn_views.chy, name='chy'),
    url(r'^chy/ChenHaiYue/', learn_views.ChenHaiYue, name='ChenHaiYue'),
    url(r'^ysl/$', learn_views.ysl, name='ysl'),
    url(r'^ysl/YangShuLin/', learn_views.YangShuLin, name='YangShuLin'),
    url(r'^ymm/$', learn_views.ymm, name='ymm'),
    url(r'^ymm/YangManMan/', learn_views.YangManMan, name='YangManMan'),
    url(r'^sxz/$', learn_views.sxz, name='sxz'),
    url(r'^sxz/SongXianZhong/', learn_views.SongXianZhong, name='SongXianZhong'),
    url(r'^test/$', learn_views.test, name='test'),
    url(r'^test/TEST/', learn_views.TEST, name='TEST'),
    url(r'^key_words_api/', learn_views.key_words_api, name='key_words_api'),
    url(r'^key_words/', learn_views.key_words, name='key_words'),
    url(r'^table/add_key_words/',learn_views.add_key_words, name='add_key_words'),
    url(r'^wanted/$', learn_views.wanted, name='wanted'),
    url(r'^wanted/wanted_json',learn_views.wanted_json, name='wanted_json'),
    url(r'^wanted/edit_sku', learn_views.edit_sku, name='edit_sku'),
    url(r'^hs_test/$', learn_views.hs_test, name='hs_test'),
    url(r'^hs_test/HS_TEST', learn_views.HS_TEST, name='HS_TEST'),
    url(r'^hs_sxb/$', learn_views.hs_sxb, name='hs_sxb'),
    url(r'^hs_sxb/HS_SXB', learn_views.HS_SXB, name='HS_SXB'),
    url(r'^hs_wq/$', learn_views.hs_wq, name='hs_wq'),
    url(r'^hs_wq/HS_WQ', learn_views.HS_WQ, name='HS_WQ'),
    url(r'^hs_chy/$', learn_views.hs_chy, name='hs_chy'),
    url(r'^hs_chy/HS_CHY', learn_views.HS_CHY, name='HS_CHY'),
    url(r'^hs_ysl/$', learn_views.hs_ysl, name='hs_ysl'),
    url(r'^hs_ysl/HS_YSL', learn_views.HS_YSL, name='HS_YSL'),
    url(r'^hs_ymm/$', learn_views.hs_ymm, name='hs_ymm'),
    url(r'^hs_ymm/HS_YMM', learn_views.HS_YMM, name='HS_YMM'),
    url(r'^hs_sxz/$', learn_views.hs_sxz, name='hs_sxz'),
    url(r'^hs_sxz/HS_SXZ', learn_views.HS_SXZ, name='HS_SXZ'),
    url(r'^shop/$', learn_views.shop, name='shop'),
    url(r'^shop/shop_json', learn_views.shop_json, name='shop_json'),
    url(r'^shop/add_user_name', learn_views.add_user_name, name='add_user_name'),
    url(r'^sp_sxb/$', learn_views.sp_sxb, name='sp_sxb'),
    url(r'^sp_wq/$', learn_views.sp_wq, name='sp_wq'),
    url(r'^sp_chy/$', learn_views.sp_chy, name='sp_chy'),
    url(r'^sp_ysl/$', learn_views.sp_ysl, name='sp_ysl'),
    url(r'^sp_ymm/$',  learn_views.sp_ymm, name='sp_ymm'),
    url(r'^sp_sxz/$', learn_views.sp_sxz, name='sp_sxz'),
    url(r'^sp_test', learn_views.sp_test, name='sp_test'),
    url(r'^sp_sxb/SP_SXB', learn_views.SP_SXB, name='SP_SXB'),
    url(r'^sp_wq/SP_WQ', learn_views.SP_WQ, name='SP_WQ'),
    url(r'^sp_chy/SP_CHY', learn_views.SP_CHY, name='SP_CHY'),
    url(r'^sp_ysl/SP_YSL', learn_views.SP_YSL, name='SP_YSL'),
    url(r'^sp_ymm/SP_YMM', learn_views.SP_YMM, name='SP_YMM'),
    url(r'^sp_sxz/SP_SXZ', learn_views.SP_SXZ, name='SP_SXZ'),
    url(r'^sp_hs_test/$', learn_views.sp_hs_test, name='sh_hs_test'),
    url(r'^sp_hs_sxb/$', learn_views.sp_hs_sxb, name='sp_hs_sxb'),
    url(r'^sp_hs_wq/$', learn_views.sp_hs_wq, name='sp_hs_wq'),
    url(r'^sp_hs_chy/$', learn_views.sp_hs_chy, name='sp_hs_chy'),
    url(r'^sp_hs_ysl/$', learn_views.sp_hs_ysl, name='sp_hs_ysl'),
    url(r'^sp_hs_ymm/$', learn_views.sp_hs_ymm, name='sp_hs_ymm'),
    url(r'^sp_hs_sxz/$', learn_views.sp_hs_sxz, name='sp_hs_sxz'),
    url(r'^sp_hs_sxb/SP_HS_SXB', learn_views.SP_HS_SXB, name='SP_HS_SXB'),
    url(r'^sp_hs_wq/SP_HS_WQ', learn_views.SP_HS_WQ, name='SP_HS_WQ'),
    url(r'^sp_hs_chy/SP_HS_CHY', learn_views.SP_HS_CHY, name='SP_HS_CHY'),
    url(r'^sp_hs_ysl/SP_HS_YSL', learn_views.SP_HS_YSL, name='SP_HS_YSL'),
    url(r'^sp_hs_ymm/SP_HS_YMM', learn_views.SP_HS_YMM, name='SP_HS_YMM'),
    url(r'^sp_hs_sxz/SP_HS_SXZ', learn_views.SP_HS_SXZ, name='SP_HS_SXZ'),
    url(r'^table/upload', learn_views.upload, name='upload'),

]
