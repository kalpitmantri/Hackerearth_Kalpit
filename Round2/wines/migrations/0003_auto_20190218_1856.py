# Generated by Django 2.1.7 on 2019-02-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0002_auto_20190218_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wines',
            name='points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wines',
            name='price',
            field=models.IntegerField(),
        ),
    ]