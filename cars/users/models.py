from django.db import models

class Users(models.Model):
    email = models.CharField(
        max_length=260,
        null=False,
        blank=False,
    )

    password = models.TextField(
        null=False,
        blank=False,
    )
