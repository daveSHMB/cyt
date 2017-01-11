from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Strip(models.Model):
    image = models.ImageField()
    alt = models.CharField(max_length=500)
    subtext = models.CharField(max_length=100000)
    pub_date = models.DateField(auto_now_add=True)

    def next(self):
        try:
            return Strip.objects.get(pk=self.pk+1)
        except:
            return None

    def previous(self):
        try:
            return Strip.objects.get(pk=self.pk-1)
        except:
            return None

class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    text = models.CharField(max_length=100000, default="")
    pub_date = models.DateField(auto_now_add=True)
