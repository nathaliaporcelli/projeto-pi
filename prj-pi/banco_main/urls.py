from django.urls import path, include
from . import views

urlpatterns = [
    #path('helloworld/', helloworld),
    path('', views.banco_main_home, name='banco-main-home'),
    path('', views.banco_main_cadastro, name='banco-main-cadastro'),
   
]