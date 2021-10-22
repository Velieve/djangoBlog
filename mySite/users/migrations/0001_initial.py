# Generated by Django 3.2.8 on 2021-10-22 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, default='', max_length=23, verbose_name='nickname')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='', max_length=6, verbose_name='gender')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='address')),
                ('image', models.ImageField(default='images/default.png', upload_to='images/%Y/%n', verbose_name='profile_img')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
