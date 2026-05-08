from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    search_fields = ['titulo', 'genero']


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer