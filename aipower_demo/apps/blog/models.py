from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "db_blog"
