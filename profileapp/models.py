from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)  # null=True : 데이터가 없어도 상관없는지 여부
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)

# terminal에서 실행할 명령어
# manage.py makemigrations
# python manage.py migrate