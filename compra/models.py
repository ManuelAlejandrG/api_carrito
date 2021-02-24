from django.db import models

# Create your models here.
class Articulo(models.Model):
    name = models.CharField(max_length=50)
    art_id = models.IntegerField()
    price = models.IntegerField()
    available_amount = models.IntegerField()

    def __str__(self):
        return self.name


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    #remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    