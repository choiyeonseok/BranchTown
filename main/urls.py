from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('/intro/', views.intropage, name='intropage'),
    path('/cs/', views.cspage, name='cspage'),


]
