# Generated by Django 2.0.2 on 2020-03-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200326_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]