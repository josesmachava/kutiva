# Generated by Django 2.0.2 on 2019-04-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20190413_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolled',
            name='course',
        ),
        migrations.AddField(
            model_name='enrolled',
            name='course',
            field=models.ManyToManyField(to='cms.Course'),
        ),
    ]
