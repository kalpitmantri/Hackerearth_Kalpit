# Generated by Django 2.1.7 on 2019-02-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0004_auto_20190218_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wines',
            name='region_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wines',
            name='region_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
