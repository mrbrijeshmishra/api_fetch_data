from django.db import models

class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=9,decimal_places=2)
    qty = models.IntegerField()