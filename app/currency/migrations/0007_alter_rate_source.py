# Generated by Django 4.0.6 on 2022-09-08 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_rate_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.source'),
        ),
    ]
