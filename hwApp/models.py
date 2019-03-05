from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ItemModel(models.Model):
    item_name = models.CharField(max_length=50, default='')
    item_fk = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.item_name
