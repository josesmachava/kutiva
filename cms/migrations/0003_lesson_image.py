# Generated by Django 2.0.2 on 2019-04-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20190423_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]