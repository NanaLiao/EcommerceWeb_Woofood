# Generated by Django 3.0.4 on 2020-04-03 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20200402_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]
