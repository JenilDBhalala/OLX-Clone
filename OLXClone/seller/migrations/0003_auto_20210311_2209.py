# Generated by Django 3.1.5 on 2021-03-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_item_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='prize',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='item',
            name='city',
            field=models.CharField(max_length=10),
        ),
    ]
