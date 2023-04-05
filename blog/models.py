from django.db import models

# Create your models here.

class Email(models.Model):
    email=models.EmailField(max_length=254)


class User(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)    
    email=models.EmailField( max_length=254)
    phone=models.PositiveIntegerField()
    message=models.TextField(null=True,blank=True)



