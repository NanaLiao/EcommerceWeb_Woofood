# Generated by Django 3.0.4 on 2020-04-03 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_remove_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
        ),
    ]
