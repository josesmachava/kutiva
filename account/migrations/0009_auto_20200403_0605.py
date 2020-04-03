# Generated by Django 2.0.2 on 2020-04-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20200403_0605'),
        ('account', '0008_auto_20200330_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='cms.Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='default-profile-2020.jpg', upload_to=''),
        ),
    ]