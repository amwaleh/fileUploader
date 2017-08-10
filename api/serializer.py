from rest_framework.serializers import ModelSerializer
from .models import File


class FileSerializer(ModelSerializer):
    '''
        Handles File upload serializer
    '''

    class Meta:
        model = File
        fields = ('id','title','file')

