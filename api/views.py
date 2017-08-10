from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import FileSerializer
from .models import File

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title','id')
