from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import File


class FileSerializer(ModelSerializer):
    '''
        Handles File upload serializer
    '''
    downloadpath= serializers.URLField(allow_blank=True, source='downloadPath', read_only=True)
    class Meta:
        model = File
        fields = ('id','title','file', 'downloadpath')


