# Generated by Django 2.1.7 on 2019-02-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wines',
            name='points',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='wines',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
