# Generated by Django 3.0.4 on 2020-04-03 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20200402_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('F', 'Fruit'), ('V', 'Vegetables'), ('M', 'Meat'), ('MK', 'Milk'), ('G', 'grocery')], max_length=2),
        ),
    ]
