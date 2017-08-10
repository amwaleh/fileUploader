from django.shortcuts import render
from rest_framework.parsers import JSONParser, MultiPartParser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import FileSerializer
from .models import File

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title','id')

class DownloadViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def retrieve(self, request, pk=None):
        queryset = File.objects.all()
        file = get_object_or_404(queryset, pk=pk)
        response = HttpResponse(file.file,content_type='image/*')
        response['Content-Disposition'] = 'attachment; filename=image.jpeg'
        return response
