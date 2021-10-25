# Generated by Django 3.2.8 on 2021-10-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211024_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='Description:'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='signa',
            field=models.TextField(blank=True, default='', max_length=100, verbose_name='Signature'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], default='', max_length=6, verbose_name='gender'),
        ),
    ]
