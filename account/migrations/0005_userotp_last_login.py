# Generated by Django 5.1 on 2024-12-17 14:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_userotp_otp_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='userotp',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
