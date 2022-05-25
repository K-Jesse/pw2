from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField()
    flavour = models.CharField(max_length=3000)
    price = models.IntegerField()

    def __str__(self):
        return self.name
