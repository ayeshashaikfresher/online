# Generated by Django 2.2.3 on 2019-11-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_merchantmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
