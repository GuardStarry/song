from django.db import models

# Create your models here.


class Article (models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Song (models.Model):
    name = models.CharField(max_length=100)
    type = models.IntegerField
    creator = models.CharField(max_length=100)
    introduce = models.TextField(blank=True, null=True)
    heat = models.IntegerField(default=0)
    imgPath = models.CharField(max_length=100)
    filePath = models.CharField(max_length=100)

    def __str__(self):
        return self.name