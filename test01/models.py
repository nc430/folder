from django.db import models


# Create your models here.
class Num_count(models.Model):
    number = models.IntegerField()

    def __int__(self):
        return self.number
