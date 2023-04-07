import uuid
from django.db import models


class User(models.Model):
    email = models.CharField(max_length=200)
    link_opened = models.BooleanField(default=False)
    compromised = models.BooleanField(default=False)
    token = models.CharField(max_length=200,default=uuid.uuid4,editable=False)


