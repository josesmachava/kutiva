# Generated by Django 2.0.2 on 2020-04-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_remove_subscription_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
