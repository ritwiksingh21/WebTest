from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=127, blank=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
