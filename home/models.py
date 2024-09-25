from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    emal=models.EmailField()
    address= models.TextField()
    # image= models.ImageField()
    # file= models.FileField()


class product(models.Model):
    product_Name= models.TextField()

class Car (models.Model):
    car_nmaer=models.CharField(max_length=100)
    speed= models.IntegerField()
    def __str__(self) -> str:
        return self.car_nmaer