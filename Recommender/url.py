"""guideForBeauty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from Recommender.handlers.user import register, logout, login, home, info
from Recommender.handlers.book import search,detail
from Recommender.handlers.userAndBook import favor, recommend


urlpatterns = [

    # 用户 user
    # # 注册
    # url(r'user/register', register.handle_register),
    # # 登录
    # url(r'user/login', login.handle_login),
    # # 保持用户登录状态
    # url(r'user/home', home.handle_home),
    # # 退出
    # url(r'user/logout', logout.handle_logout),
    # # 用户信息
    # url(r'user/info', info.handle_logout),

    # 书本
    url(r'book/search', search.handle_search),
    # url(r'book/hot', info.handle_logout),
    url(r'book/detail', detail.handle_book_detail),


    # 喜爱列表
    # add
    url(r'favor/add', favor.handle_favor_add),
    url(r'favor/query', favor.handle_favor_query),
    url(r'favor/delete', favor.handle_favor_delete),

    url(r'star/query', favor.handle_favor_star_query)


]