# Generated by Django 4.2.3 on 2023-07-23 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flash_app', '0011_remove_follower_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]