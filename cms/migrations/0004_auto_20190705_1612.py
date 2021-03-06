# Generated by Django 2.0.2 on 2019-07-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_lesson_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('url', models.URLField()),
                ('icon', models.FileField(upload_to='icons')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
