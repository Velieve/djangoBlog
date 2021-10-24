# Generated by Django 3.2.8 on 2021-10-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Verify code.')),
                ('email', models.EmailField(max_length=35, verbose_name='email')),
                ('send_type', models.CharField(choices=[('register', 'register'), ('forget', 'forget')], default='register', max_length=10)),
            ],
            options={
                'verbose_name': 'Email verification',
                'verbose_name_plural': 'Email verifications',
            },
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Username', 'verbose_name_plural': 'Usernames'},
        ),
    ]