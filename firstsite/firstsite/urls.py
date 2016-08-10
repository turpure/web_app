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
    url(r'^index/key_words_json', learn_views.key_words_json, name='test_kw'),
    url(r'^add/$', learn_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^product/$', learn_views.product, name='product'),
    url(r'^sxb/', learn_views.sxb, name='sxb'),
    url(r'^ShangXianBei/', learn_views.ShangXianBei, name='ShangXianBei'),
    url(r'^wq/', learn_views.wq, name='wq'),
    url(r'^WuQiong/', learn_views.WuQiong, name='WuQing'),
    url(r'^chy/', learn_views.chy, name='chy'),
    url(r'^ChenHaiYue/', learn_views.ChenHaiYue, name='ChenHaiYue'),
    url(r'^ysl/', learn_views.ysl, name='ysl'),
    url(r'^YangShuLin/', learn_views.YangShuLin, name='YangShuLin'),
    url(r'^ymm/', learn_views.ymm, name='ymm'),
    url(r'^YangManMan/', learn_views.YangManMan, name='YangManMan'),
    url(r'^sxz/', learn_views.sxz, name='sxz'),
    url(r'^SongXianZhong/', learn_views.SongXianZhong, name='SongXianZhong'),
    url(r'^key_words_api/', learn_views.key_words_api, name='key_words_api'),
    url(r'^key_words/', learn_views.key_words, name='key_words')
]
