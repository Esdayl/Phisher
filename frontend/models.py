import uuid
from django.db import models


class User(models.Model):
    email = models.CharField(max_length=200)
    link_opened = models.BooleanField(default=False)
    compromised = models.BooleanField(default=False)
    has_reported = models.BooleanField(default=False)
    click_date = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=200,default=uuid.uuid4,editable=False)


