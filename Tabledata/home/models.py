from django.db import models

# Create your models here.
class Sdata(models.Model):
    Name = models.CharField(max_length=32)
    Qualification = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    YOP = models.IntegerField()
    Age = models.IntegerField()
    Skills = models.CharField(max_length=30)
    DOB = models.DateField(max_length=20)
    Address = models.CharField(max_length=10)
    Mock_Rating = models.CharField(max_length=10)
    Department = models.CharField(max_length=20)

    def __str__(self):
        return self.name