from django.db import models

from utils.models import CuidField


# Create your models here.


class SomeModel(models.Model):
    id = CuidField(primary_key=True, prefix="model_")

    def __str__(self):
        return self.id
