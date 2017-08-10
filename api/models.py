import os
from django.db import models
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    # Validates the file type
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg','.jpg','.gif']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')

class File(models.Model):
    '''
         Handles file upload Model
    '''
    title= models.TextField(blank=True)
    file= models.FileField(blank=False, upload_to='uploads/', validators=[validate_file_extension])

