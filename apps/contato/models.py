from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    fone = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=100,
        
    )
