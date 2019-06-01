from django.db import models
from django.db.models import deletion
from django.db.models.aggregates import Sum
from django.db.models.deletion import PROTECT
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
from embed_video.fields import EmbedVideoField

from wykop.accounts.models import User


class Post(models.Model):
    title = models.CharField(default='', max_length=150)
    content = models.TextField(default='')
    author = models.ForeignKey(User, related_name='posts', on_delete = deletion.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True)
    video = EmbedVideoField(default='', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    def score(self):
        return self.votes.aggregate(score=Sum('value'))['score'] or 0

class Vote(models.Model):
    class Meta:
        unique_together = (('user', 'post'), )

    PLUS = 1
    MINUS = -1
    VALUE_CHOICES = (
        (PLUS, '+'),
        (MINUS, '-')
    )

    value = models.IntegerField(choices=VALUE_CHOICES)
    post = models.ForeignKey(Post, related_name='votes', on_delete = deletion.PROTECT)
    user = models.ForeignKey(User, related_name='votes', on_delete = deletion.PROTECT)

    def __str__(self):
        return '({}) {} - {}'.format(
            self.get_value_display(),
            self.user,
            self.post
        )

class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete = deletion.PROTECT)
    user = models.ForeignKey(User, related_name='comments', on_delete = deletion.PROTECT)
    text = models.TextField(default='')