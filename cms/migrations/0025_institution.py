# Generated by Django 2.0.2 on 2020-04-04 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_auto_20200404_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
