# Generated by Django 2.0.2 on 2019-04-28 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20190428_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='limit_date',
            new_name='last_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='registed_at',
        ),
        migrations.AddField(
            model_name='payment',
            name='start_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]