# Generated by Django 3.1.4 on 2021-05-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_user',
            name='login',
            field=models.CharField(default='SOMESTRING', max_length=50),
        ),
        migrations.AddField(
            model_name='chat_user',
            name='password',
            field=models.CharField(default='SOMESTRING', max_length=50),
        ),
    ]
