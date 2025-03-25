from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    content1 = models.CharField(max_length=100)
    content2 = models.CharField(max_length=100)
