from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^receitas/$', views.ReceitasList.as_view(), name='receitas-list'),

]