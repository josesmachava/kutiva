# Generated by Django 2.0.2 on 2019-04-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190428_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
