from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Images')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

# class Destination(models.Model):
#     id: int
#     name: str
#     img: str
#     desc: str
#     price: int
#     offer: bool