# Generated by Django 3.1.4 on 2021-05-23 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210519_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='authorization',
            fields=[
                ('chat_user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.chat_user')),
            ],
            bases=('main.chat_user',),
        ),
    ]