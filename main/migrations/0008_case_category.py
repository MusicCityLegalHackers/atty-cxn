# Generated by Django 2.0.4 on 2018-04-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_attorney_is_next'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.CharField(default='Divorce', max_length=30),
            preserve_default=False,
        ),
    ]
