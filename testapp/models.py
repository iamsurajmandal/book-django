from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=64);
    desc=models.CharField(max_length=64);
    genre=models.CharField(max_length=64);
    rating=models.FloatField();
    author=models.CharField(max_length=64);
    def __str__(self):
        return self.title


# Create your models here.
