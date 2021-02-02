from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 20)
    qty = models.IntegerField()

    def _str_ (self):
        return self.title