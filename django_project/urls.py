from django.contrib import admin
from django.urls import path
from .views import investment_home, investment_detail, investment_list, simple_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', investment_home, name='home'),
    path('detail/', investment_detail, name='detail'),
    path('list/', investment_list, name='list'),
    path('test/', simple_test, name='test'),
]
