from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Marka(models.Model):
    marka_name = models.CharField(max_length=32)

    def __str__(self):
        return self.marka_name

class Model(models.Model):
    model_name = models.CharField(max_length=32)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

class Car(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900, "Год не может быть меньше 1900"),
            MaxValueValidator(datetime.date.today().year, "Год не может быть больше текущего")
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=30)
    volume = models.FloatField()
    type_change = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
