from django.db import models

# Create your models here.
class Dht11(models.Model):
 temp = models.FloatField(null=True)
 hum = models.FloatField(null=True)
 dt = models.DateTimeField(auto_now_add=True,null=True)
