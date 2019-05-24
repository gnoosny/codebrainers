from django.db import models
from django.db.models import deletion
from django.db.models.deletion import PROTECT

from wykop.accounts.models import User


class Post(models.Model):
    title = models.CharField(default='', max_length=150)
    content = models.TextField(default='')
    author = models.ForeignKey(User, related_name='posts', on_delete = deletion.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title