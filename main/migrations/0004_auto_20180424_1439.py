# Generated by Django 2.0.4 on 2018-04-24 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180419_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='phone',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attorney',
            name='state',
            field=models.CharField(default='TN', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(default='TN', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='legaldoc',
            name='date_submitted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
