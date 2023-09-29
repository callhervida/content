from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    """A Model for blog post's information including content's title, content
    author and Publication Date"""

    title = models.CharField(blank=True, null=True, max_length=100)

    content = models.TextField(blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="تاریخ ایجاد")
