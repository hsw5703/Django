from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)  # on_delete 구문에서 연결돼 있는 Article이 삭제되면 comment는 일단 남아있게 설정
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    content = models.TextField(null=False)  # 장문의 경우 TextField, 단문의 경우 CharField 사용
    created_at = models.DateTimeField(auto_now_add=True)