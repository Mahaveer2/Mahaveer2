from django.db import models

# Create your models here.
class Posts(models.Model):
    post = models.TextField()
    time = models.DateTimeField(auto_now = True)