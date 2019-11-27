# Generated by Django 2.2.3 on 2019-11-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantModel',
            fields=[
                ('idno', models.IntegerField(default=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]