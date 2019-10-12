from django.db import models

# Create your models here.

class Register(models.Model):
    nom = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    repass = models.CharField(max_length=8)
    email = models.EmailField()
    contact = models.CharField(max_length=8)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
