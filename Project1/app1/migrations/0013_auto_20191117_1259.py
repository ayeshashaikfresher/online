# Generated by Django 2.2.3 on 2019-11-17 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20191117_1112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MerchantModel',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]