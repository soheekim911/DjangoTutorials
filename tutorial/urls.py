"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from community.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write, name='write'), # views.py에 있는 write라는 함수를 통해 뭔가 할 수 있다
    path('list/', list, name='list'),
    path('view/<int:num>/', view), # 정규표현식 숫자를 num이라는 인자로 받아서, views.py의 view 함수에서 사용
    path('ajax/demo1/', curtime, name='curtime'),
    path('ajax/demo2/', timeselect, name='timeselect'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
]
