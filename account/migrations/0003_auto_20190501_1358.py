# Generated by Django 2.0.2 on 2019-05-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190501_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]