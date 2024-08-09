from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models import CuidField
from utils.upload_path import upload_image_path


# Create your models here.

class User(AbstractUser):
    id = CuidField(primary_key=True, prefix="user_")

    # oidc id
    sub = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    profile_img = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    # Add extras
