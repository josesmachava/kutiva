# Generated by Django 2.0.2 on 2020-04-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200404_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='default-profile-2020.jpg', upload_to='photo'),
        ),
    ]
