# Generated by Django 3.1.5 on 2021-03-31 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_auto_20210331_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='seller_id',
            field=models.IntegerField(),
        ),
    ]
