# Generated by Django 2.0.2 on 2020-04-04 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20200403_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='expired_date',
            field=models.DateField(default=datetime.date(2020, 5, 4)),
        ),
    ]
