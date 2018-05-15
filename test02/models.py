from django.db import models

# Create your models here.
class num2Count(models.Model):
    number = models.IntegerField()

    def __int__(self):
        return self.number