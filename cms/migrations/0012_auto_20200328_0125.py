# Generated by Django 2.0.2 on 2020-03-27 23:25

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20200328_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]
