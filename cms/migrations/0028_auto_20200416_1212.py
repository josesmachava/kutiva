# Generated by Django 2.0.2 on 2020-04-16 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0027_auto_20200415_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='expired_date',
            field=models.DateField(default=datetime.date(2020, 5, 16)),
        ),
    ]
