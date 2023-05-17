from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    image = models.ImageField(verbose_name="이미지", null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    content = models.TextField(verbose_name="댓글")
    created_at = models.DateTimeField(verbose_name="작성일")
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)