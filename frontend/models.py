from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)
    link_opened = models.BooleanField(null=True)
    compromised = models.BooleanField(null=True)
    token = models.CharField(max_length=200)


