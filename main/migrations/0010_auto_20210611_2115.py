# Generated by Django 3.1.4 on 2021-06-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_chat_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_message',
            name='sender',
            field=models.CharField(default='SOMESTRING', max_length=300),
        ),
    ]
