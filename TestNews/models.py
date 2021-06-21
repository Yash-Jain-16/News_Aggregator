from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    image=models.URLField(max_length=500)


