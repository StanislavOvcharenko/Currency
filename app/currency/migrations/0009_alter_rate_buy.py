# Generated by Django 4.0.6 on 2022-09-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_alter_rate_currency_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='buy',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]