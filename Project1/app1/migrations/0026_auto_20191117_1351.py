# Generated by Django 2.2.3 on 2019-11-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_auto_20191117_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModelNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='AdminModel',
        ),
    ]
