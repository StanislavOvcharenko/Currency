# Generated by Django 4.0.6 on 2022-10-26 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0011_alter_source_bank_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]