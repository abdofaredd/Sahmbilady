from django.db import models

# Create your models here.
class School (models.Model):
    school_group=models.CharField(max_length=10,null=True, blank=True)
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    address=models.CharField(max_length=500,null=True, blank=True)
    # photo=models.ImageField(upload_to='images')