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
    desc = models.TextField('Description:', max_length=200,blank=True,default='')
    signa = models.TextField('Signature',max_length=100,blank=True,default='')
    birthday = models.DateField('birthday', null=True, blank=True)
    gender = models.CharField('gender', max_length=6,
                              choices=USER_GENDER_TYPE, default='')
    address = models.CharField(
        'address', max_length=100, blank=True, default='')
    image = models.ImageField(
        upload_to='images/%Y/%n', default='images/default.png', max_length=100, verbose_name='profile_img')

    class Meta:
        verbose_name = 'Username'
        verbose_name_plural = verbose_name + 's'
    
    def __str__(self) -> str:
        return self.owner.username

class EmailVerifyRecord(models.Model):
    SEND_TYPE_CHOICE=(
        ('register','register'),
        ('forget','forget')
    )
    code = models.CharField('Verify code.',max_length=20)
    email = models.EmailField('email',max_length=35)
    send_type = models.CharField(choices=SEND_TYPE_CHOICE,max_length=10,default='register')

    class Meta:
        verbose_name = 'Email verification'
        verbose_name_plural = verbose_name + 's'
    
    def __str__(self):
        return self.code
