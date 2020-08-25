from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    objects = models.manager
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.content

    #CASCADE; 종속, 모델이 삭제되면 함께 삭제된다. 게시한 post가 삭제되면 댓글도 함께 삭제된다. 
    #auto_now_add ; admin에 저장하는 시간을 자동으로 저장; auto_now ; 시간 수정 가능