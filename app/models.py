from django.db import models

# Create your models here.
#I am Chouchou's dandan,love u hahh.

class Article (models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date_time']