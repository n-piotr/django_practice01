from django.db import models


# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    power = models.IntegerField()
    type = models.CharField(max_length=50)
    kms = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return str(self.title)
