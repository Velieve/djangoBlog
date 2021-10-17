from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.


class UserProfile(models.Model):
    USER_GENDER_TYPE = {
        ('male', '男'),
        ('female', '女')
    }

    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='user')
    nickname = models.CharField(
        'nickname', max_length=23, blank=True, default='')
    birthday = models.DateField('birthday', null=True, blank=True)
    gender = models.CharField('gender', max_length=6,
                              choices=USER_GENDER_TYPE, default='')
    address = models.CharField(
        'address', max_length=100, blank=True, default='')
    image = models.ImageField(
        upload_to='images/%Y/%n', default='images/default.png', max_lenght=100, verbose_name='profile_img')
    