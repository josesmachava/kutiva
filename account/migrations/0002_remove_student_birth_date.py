# Generated by Django 2.0.2 on 2019-12-03 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='birth_date',
        ),
    ]
