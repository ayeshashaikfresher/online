# Generated by Django 2.2.3 on 2019-11-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_product_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name=10),
        ),
    ]
