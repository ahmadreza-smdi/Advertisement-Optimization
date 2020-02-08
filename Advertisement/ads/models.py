from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=50)
    des = models.CharField(max_length=200)
    def __str__(self):
        return self.url


class Adv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.CharField(max_length=2000)
    Related_website_url = models.CharField(max_length=200)
    def __str__(self):
        return self.Related_website_url