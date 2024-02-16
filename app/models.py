from django.db import models

# Create your models here.
class Book(models.Model):
    bid=models.IntegerField(primary_key=True)
    bname=models.CharField(max_length=100)
    bauthor=models.CharField(max_length=100)

    def __str__(self):
        return self.bname