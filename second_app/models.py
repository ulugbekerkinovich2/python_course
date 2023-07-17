from django.db import models


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=50)
    domain = models.URLField()

    def __str__(self):
        return self.name
