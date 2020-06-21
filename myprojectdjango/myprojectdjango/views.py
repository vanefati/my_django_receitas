from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Receita
from .serializers import ReceitaSerializer

# Create your views here.
class ReceitasList(generics.ListCreateAPIView):

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer