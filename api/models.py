from django.db import models


class File(models.Model):
    '''
         Handles file upload Model
    '''
    title= models.TextField(blank=True)
    file= models.FileField(blank=False, upload_to='uploads/')