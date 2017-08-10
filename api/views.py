from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import FileSerializer
from .models import File

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer